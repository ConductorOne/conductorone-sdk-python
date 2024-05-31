"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .approval import Approval
from .approvedaction import ApprovedAction
from .deniedaction import DeniedAction
from .reassignedaction import ReassignedAction
from .reassignedbyerroraction import ReassignedByErrorAction
from .restartaction import RestartAction
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


class ApprovalInstanceState(str, Enum):
    r"""The state of the approval instance"""
    APPROVAL_INSTANCE_STATE_UNSPECIFIED = 'APPROVAL_INSTANCE_STATE_UNSPECIFIED'
    APPROVAL_INSTANCE_STATE_INIT = 'APPROVAL_INSTANCE_STATE_INIT'
    APPROVAL_INSTANCE_STATE_SENDING_NOTIFICATIONS = 'APPROVAL_INSTANCE_STATE_SENDING_NOTIFICATIONS'
    APPROVAL_INSTANCE_STATE_WAITING = 'APPROVAL_INSTANCE_STATE_WAITING'
    APPROVAL_INSTANCE_STATE_DONE = 'APPROVAL_INSTANCE_STATE_DONE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ApprovalInstance:
    r"""The approval instance object describes the way a policy step should be approved as well as its outcomes and state.

    This message contains a oneof named outcome. Only a single field of the following list may be set at a time:
      - approved
      - denied
      - reassigned
      - restarted
      - reassignedByError
    """
    UNSET='__SPEAKEASY_UNSET__'
    approval: Optional[Approval] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approval'), 'exclude': lambda f: f is ApprovalInstance.UNSET }})
    r"""The Approval message.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
      - users
      - manager
      - appOwners
      - group
      - self
      - entitlementOwners
      - expression
    """
    approved_action: Optional[ApprovedAction] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approved'), 'exclude': lambda f: f is ApprovalInstance.UNSET }})
    r"""The approved action indicates that the approvalinstance had an outcome of approved."""
    denied_action: Optional[DeniedAction] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('denied'), 'exclude': lambda f: f is ApprovalInstance.UNSET }})
    r"""The denied action indicates that the c1.api.policy.v1.ApprovalInstance had an outcome of denied."""
    reassigned_action: Optional[ReassignedAction] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reassigned'), 'exclude': lambda f: f is ApprovalInstance.UNSET }})
    r"""The ReassignedAction object describes the outcome of a policy step that has been reassigned."""
    reassigned_by_error_action: Optional[ReassignedByErrorAction] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reassignedByError'), 'exclude': lambda f: f is ApprovalInstance.UNSET }})
    r"""The ReassignedByErrorAction object describes the outcome of a policy step that has been reassigned because it had an error provisioning."""
    restart_action: Optional[RestartAction] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('restarted'), 'exclude': lambda f: f is ApprovalInstance.UNSET }})
    r"""The restart action describes the outcome of policy steps for when the task was restarted. This can be applied to multiple steps since restart skips all pending next steps."""
    state: Optional[ApprovalInstanceState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""The state of the approval instance"""
    

