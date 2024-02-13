"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .tasktypecertify import TaskTypeCertify
from .tasktypegrant import TaskTypeGrant
from .tasktyperevoke import TaskTypeRevoke
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskType:
    r"""Task Type provides configuration for the type of task: certify, grant, or revoke

    This message contains a oneof named task_type. Only a single field of the following list may be set at a time:
      - grant
      - revoke
      - certify
    """
    UNSET='__SPEAKEASY_UNSET__'
    task_type_certify: Optional[TaskTypeCertify] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certify'), 'exclude': lambda f: f is TaskType.UNSET }})
    r"""The TaskTypeCertify message indicates that a task is a certify task and all related details."""
    task_type_grant: Optional[TaskTypeGrant] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grant'), 'exclude': lambda f: f is TaskType.UNSET }})
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    task_type_revoke: Optional[TaskTypeRevoke] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revoke'), 'exclude': lambda f: f is TaskType.UNSET }})
    r"""The TaskTypeRevoke message indicates that a task is a revoke task and all related details."""
    

