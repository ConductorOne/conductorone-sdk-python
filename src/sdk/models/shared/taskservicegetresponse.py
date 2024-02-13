"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .taskview import TaskView
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskServiceGetResponseExpanded:
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    UNSET='__SPEAKEASY_UNSET__'
    at_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    r"""The type of the serialized message."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskServiceGetResponse:
    r"""The TaskServiceGetResponse returns a task view which has a task including JSONPATHs to the expanded items in the expanded array."""
    UNSET='__SPEAKEASY_UNSET__'
    task_view: Optional[TaskView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taskView'), 'exclude': lambda f: f is None }})
    r"""Contains a task and JSONPATH expressions that describe where in the expanded array related objects are located. This view can be used to display a fully-detailed dashboard of task information."""
    expanded: Optional[List[TaskServiceGetResponseExpanded]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expanded'), 'exclude': lambda f: f is TaskServiceGetResponse.UNSET }})
    r"""List of serialized related objects."""
    

