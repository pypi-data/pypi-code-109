# Copyright 2019, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Training loops for iterative process simulations."""

import collections
import time
from typing import Any, Callable, Iterable, Mapping, MutableMapping, Optional, Tuple

from absl import logging

from tensorflow_federated.python.common_libs import structure
from tensorflow_federated.python.core.api import computation_base
from tensorflow_federated.python.core.templates import iterative_process
from tensorflow_federated.python.program import program_state_manager as program_state_manager_lib
from tensorflow_federated.python.program import release_manager as release_manager_lib

MetricsType = MutableMapping[str, Any]

ROUND_TIME_KEY = 'round_time_in_seconds'

ROUND_NUMBER_KEY = 'round_number'
TRAINING_TIME_KEY = 'training_time_in_seconds'
EVALUATION_METRICS_PREFIX = 'evaluation/'
EVALUATION_TIME_KEY = 'evaluation_time_in_seconds'


def run_stateless_simulation(computation: computation_base.Computation,
                             client_selection_fn: Callable[[int], Any],
                             total_rounds: int,
                             metrics_managers: Optional[Iterable[
                                 release_manager_lib.ReleaseManager]] = None):
  """Runs a federated computation on a given set of client data.

  This method performs `total_rounds` calls to the `computation`. At each round,
  this method samples client data via `client_selection_fn(round_num)`, and uses
  this as input to `computation`. The output of `computation` is assumed to be
  a mutable mapping with string-valued keys.

  This method also records how long it takes (in seconds) to call
  `client_selection_fn` and `computation` at each round and adds this to a
  dictionary of  round metrics with key `tff.simulation.ROUND_TIME_KEY`.

  Args:
    computation: A `tff.Computation` to be executed. Must accept a single
      argument (placed or unplaced).
    client_selection_fn: Callable accepting an integer round number, and
      returning a list of client data to use as federated data for that round.
    total_rounds: The number of federated training rounds to perform.
    metrics_managers: An optional list of `tff.program.ReleaseManagers`s to use
      to save metrics.

  Returns:
    An dictionary, keyed by round number, with values corresponding to the
      outputs of each round's computation, with extra keys for timing
      information.
  """
  # TODO(b/194841884): Add an optional checkpoint manager argument once the
  # checkpoint managers have compatibility with "stateless" structures.
  start_round = 0

  all_metrics = collections.OrderedDict()
  for round_num in range(start_round, total_rounds):
    round_metrics = collections.OrderedDict(round_num=round_num)
    computation_start_time = time.time()

    federated_data = client_selection_fn(round_num)
    output = computation(federated_data)
    computation_time = time.time() - computation_start_time
    logging.info('Computation completed, took %.4f seconds', computation_time)

    round_metrics.update(output)
    round_metrics[ROUND_TIME_KEY] = computation_time

    if metrics_managers is not None:
      for metrics_manager in metrics_managers:
        metrics_manager.release(round_metrics, round_num)

    all_metrics[round_num] = round_metrics

  return all_metrics


def _run_training(training_fn: computation_base.Computation,
                  client_selection_fn: Callable[[int], Any], state: Any,
                  round_num: int) -> Tuple[Any, Mapping[str, Any]]:
  """Runs one round of federated training."""
  logging.info('Running training at round %d', round_num)
  metrics = collections.OrderedDict()
  training_time_start = time.time()
  training_data = client_selection_fn(round_num)
  state, training_metrics = structure.from_container(
      training_fn(state, training_data))
  training_time = time.time() - training_time_start
  metrics.update(training_metrics)
  metrics[TRAINING_TIME_KEY] = training_time
  metrics[ROUND_NUMBER_KEY] = round_num
  return state, metrics


def _run_evaluation(evaluation_fn: Callable[[Any, Any], MetricsType],
                    client_selection_fn: Callable[[int], Any], state: Any,
                    round_num: int) -> Mapping[str, Any]:
  """Runs one round of federated evaluation."""
  logging.info('Running evaluation at round %d', round_num)
  metrics = collections.OrderedDict()
  evaluation_time_start = time.time()
  evaluation_data = client_selection_fn(round_num)
  evaluation_metrics = evaluation_fn(state, evaluation_data)
  evaluation_time = time.time() - evaluation_time_start
  metrics.update(evaluation_metrics)
  metrics[EVALUATION_TIME_KEY] = evaluation_time
  return {EVALUATION_METRICS_PREFIX + k: v for (k, v) in metrics.items()}


def run_training_process(
    training_process: iterative_process.IterativeProcess,
    training_selection_fn: Callable[[int], Any],
    total_rounds: int,
    evaluation_fn: Optional[Callable[[Any, Any], MetricsType]] = None,
    evaluation_selection_fn: Optional[Callable[[int], Any]] = None,
    rounds_per_evaluation: int = 1,
    program_state_manager: Optional[
        program_state_manager_lib.ProgramStateManager] = None,
    rounds_per_saving_program_state: int = 1,
    metrics_managers: Optional[Iterable[
        release_manager_lib.ReleaseManager]] = None):
  """Runs a federated `training_process`.

  The following `tff.Computation` types signaures are required:

  *   `training_process.initialize`: `( -> state)`.
  *   `training_process.next`: `<state, client_data> -> <state, metrics>`
  *   `evaulation_fn`:  `<state, client_data> -> metrics`

  This function performs up to `total_rounds` updates to the `state` of the
  given `training_process`. At each training round, this update occurs by
  invoking `training_process.next` with `state` and the output of
  `training_selection_fn`. Depending on `rounds_per_evaluation` and
  `rounds_per_saving_program_state`, each training round may be followed by an
  invocation of the `evaluation_fn` and by saving the program state.

  Note: Round 0 represents saving an initial program model state and computing
  initial evaluation metrics and round 1 through total_rounds + 1 represent the
  training rounds.

  In addition to the training metrics and evaluation metrics, this function adds
  the following performance metrics (key and descriptions):

  * tff.simulation.ROUND_NUMBER_KEY: The round number.
  * tff.simulation.TRAINING_TIME_KEY: The amount of time (in seconds) it takes
    to run one round of training.
  * tff.simulation.EVALUATION_TIME_KEY: The amount of time (in seconds) it takes
    to run one round of evaluation.

  Args:
    training_process: A `tff.templates.IterativeProcess` to run for training.
    training_selection_fn: A `Callable` accepting an integer round number, and
      returning a list of client data to use for trainig in that round.
    total_rounds: The number of training rounds to run.
    evaluation_fn: An optional callable accepting the state of
      `training_process` and the output of `evaluation_selection_fn`, and
      returning a mutable mapping with string-valued keys.
    evaluation_selection_fn: A optional `Callable` accepting an integer round
      number, and returning a list of client data to use for evaluation in that
      round.
    rounds_per_evaluation: The number of training rounds to run between each
      invocation of `evaluation_fn`.
    program_state_manager: An optional `tff.program.ProgramStateManager` to use
      to save program state for fault tolerance.
    rounds_per_saving_program_state: The number of training rounds to run
      between saving program state.
    metrics_managers: An optional list of `tff.program.ReleaseManagers`s to use
      to save metrics.

  Returns:
    The `state` of the training process after training.
  """
  logging.info('Running training process')
  if program_state_manager is not None:
    training_process_structure = training_process.initialize()
    program_state, previous_saved_version = program_state_manager.load_latest(
        training_process_structure)
  else:
    program_state = None
  if program_state is not None:
    logging.info('Loaded program state at version %d', previous_saved_version)
    state = program_state
    start_round = previous_saved_version + 1
  else:
    logging.info('Initializing training process')
    state = training_process.initialize()
    start_round = 1

    if evaluation_fn is not None and evaluation_selection_fn is not None:
      evaluation_metrics = _run_evaluation(evaluation_fn,
                                           evaluation_selection_fn, state, 0)

      if metrics_managers is not None:
        for metrics_manager in metrics_managers:
          metrics_manager.release(evaluation_metrics, 0)

    if program_state_manager is not None:
      program_state_manager.save(state, 0)

  for round_num in range(start_round, total_rounds + 1):
    logging.info('Starting round %d', round_num)
    round_metrics = collections.OrderedDict()
    state, training_metrics = _run_training(training_process.next,
                                            training_selection_fn, state,
                                            round_num)
    round_metrics.update(training_metrics)

    if evaluation_fn is not None and evaluation_selection_fn is not None:
      if round_num % rounds_per_evaluation == 0:
        evaluation_metrics = _run_evaluation(evaluation_fn,
                                             evaluation_selection_fn, state,
                                             round_num)
        round_metrics.update(evaluation_metrics)

    if metrics_managers is not None:
      for metrics_manager in metrics_managers:
        metrics_manager.release(round_metrics, round_num)

    if program_state_manager is not None:
      if round_num % rounds_per_saving_program_state == 0:
        program_state_manager.save(state, round_num)

  return state
