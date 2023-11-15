"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .tasktypecertify_input import TaskTypeCertifyInput
from .tasktypegrant_input import TaskTypeGrantInput
from .tasktyperevoke_input import TaskTypeRevokeInput
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskTypeInput:
    r"""Task Type provides configuration for the type of task: certify, grant, or revoke

    This message contains a oneof named task_type. Only a single field of the following list may be set at a time:
      - grant
      - revoke
      - certify
    """
    task_type_certify: Optional[TaskTypeCertifyInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certify') }})
    r"""The TaskTypeCertify message indicates that a task is a certify task and all related details."""
    task_type_grant: Optional[TaskTypeGrantInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grant') }})
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    task_type_revoke: Optional[TaskTypeRevokeInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revoke') }})
    r"""The TaskTypeRevoke message indicates that a task is a revoke task and all related details."""
    

