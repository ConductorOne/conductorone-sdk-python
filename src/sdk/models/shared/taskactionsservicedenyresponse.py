"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import taskview as shared_taskview
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskActionsServiceDenyResponse:
    r"""The TaskActionsServiceDenyResponse returns a task view with paths indicating the location of expanded items in the array."""
    expanded: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expanded'), 'exclude': lambda f: f is None }})
    r"""List of serialized related objects."""
    task_view: Optional[shared_taskview.TaskView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taskView'), 'exclude': lambda f: f is None }})
    r"""Contains a task and JSONPATH expressions that describe where in the expanded array related objects are located. This view can be used to display a fully-detailed dashboard of task information."""
    ticket_action_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ticketActionId'), 'exclude': lambda f: f is None }})
    r"""The ID of the ticket (task) deny action created by this request."""
    

