# Copyright 2022, The TensorFlow Federated Authors.
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
"""A library of `tf.keras.metrics.Metrics` for learning."""

import tensorflow as tf


class NumExamplesCounter(tf.keras.metrics.Sum):
  """A `tf.keras.metrics.Metric` that counts the number of examples seen.

  NOTE: This metric ignores sample weighting, counting each example uniformly.
  """

  def __init__(self, name='num_examples', dtype=tf.int64):  # pylint: disable=useless-super-delegation
    super().__init__(name, dtype)

  def update_state(self, y_true, y_pred, sample_weight=None):
    return super().update_state(tf.shape(y_pred)[0], sample_weight=None)


class NumBatchesCounter(tf.keras.metrics.Sum):
  """A `tf.keras.metrics.Metric` that counts the number of batches seen.

  NOTE: This metric ignores sample weighting, counting each batch uniformly.
  """

  def __init__(self, name='num_batches', dtype=tf.int64):  # pylint: disable=useless-super-delegation
    super().__init__(name, dtype)

  def update_state(self, y_true, y_pred, sample_weight=None):
    return super().update_state(1, sample_weight=None)
