# Copyright 2021 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the GNU Affero General Public License 3.0 (the "License").
# A copy of the License may be obtained with this software package or at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html
#
# Use of this file is prohibited except in compliance with the License. Any
# modifications or derivative works of this file must retain this copyright
# notice, and modified files must contain a notice indicating that they have
# been altered from the originals.
#
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
#
# Relief from the License may be granted by purchasing a commercial license.


from dataclasses import dataclass
from typing import Any, Dict, NamedTuple


@dataclass
class Status:
    STATUS: str

    def __bool__(self):
        """
        Return True if the status is not "NEW_OBJECT"
        """

        return self.STATUS != "NEW_OBJECT"

    def __str__(self) -> str:
        return self.STATUS


class RESULT_STATUS:
    NEW_OBJECT = Status("NEW_OBJECT")
    COMPLETED = Status("COMPLETED")
    FAILED = Status("FAILED")
    RUNNING = Status("RUNNING")
    CANCELLED = Status("CANCELLED")


class TaskExecutionMetadata(NamedTuple):
    """
    Metadata about a task execution.

    Attributes:
        selected_executor: The name of the executor that was selected for this task.
        execution_args: The arguments that were passed to the executor.
    """

    selected_executor: Any
    execution_args: Dict


class DispatchInfo(NamedTuple):
    """
    Information about a dispatch to be shared to a task post dispatch.

    Attributes:
        dispatch_id: Dispatch id of the dispatch.
    """

    dispatch_id: str
