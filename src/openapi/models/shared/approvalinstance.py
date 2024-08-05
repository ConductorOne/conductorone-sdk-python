"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .approval import Approval, ApprovalTypedDict
from .approvedaction import ApprovedAction, ApprovedActionTypedDict
from .deniedaction import DeniedAction, DeniedActionTypedDict
from .reassignedaction import ReassignedAction, ReassignedActionTypedDict
from .reassignedbyerroraction import ReassignedByErrorAction, ReassignedByErrorActionTypedDict
from .restartaction import RestartAction, RestartActionTypedDict
from enum import Enum
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ApprovalInstanceState(str, Enum):
    r"""The state of the approval instance"""
    APPROVAL_INSTANCE_STATE_UNSPECIFIED = "APPROVAL_INSTANCE_STATE_UNSPECIFIED"
    APPROVAL_INSTANCE_STATE_INIT = "APPROVAL_INSTANCE_STATE_INIT"
    APPROVAL_INSTANCE_STATE_SENDING_NOTIFICATIONS = "APPROVAL_INSTANCE_STATE_SENDING_NOTIFICATIONS"
    APPROVAL_INSTANCE_STATE_WAITING = "APPROVAL_INSTANCE_STATE_WAITING"
    APPROVAL_INSTANCE_STATE_DONE = "APPROVAL_INSTANCE_STATE_DONE"

class ApprovalInstanceTypedDict(TypedDict):
    r"""The approval instance object describes the way a policy step should be approved as well as its outcomes and state.

    This message contains a oneof named outcome. Only a single field of the following list may be set at a time:
    - approved
    - denied
    - reassigned
    - restarted
    - reassignedByError

    """
    
    approval: NotRequired[Nullable[ApprovalTypedDict]]
    r"""The Approval message.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
    - users
    - manager
    - appOwners
    - group
    - self
    - entitlementOwners
    - expression
    - webhook

    """
    approved_action: NotRequired[Nullable[ApprovedActionTypedDict]]
    r"""The approved action indicates that the approvalinstance had an outcome of approved."""
    denied_action: NotRequired[Nullable[DeniedActionTypedDict]]
    r"""The denied action indicates that the c1.api.policy.v1.ApprovalInstance had an outcome of denied."""
    reassigned_action: NotRequired[Nullable[ReassignedActionTypedDict]]
    r"""The ReassignedAction object describes the outcome of a policy step that has been reassigned."""
    reassigned_by_error_action: NotRequired[Nullable[ReassignedByErrorActionTypedDict]]
    r"""The ReassignedByErrorAction object describes the outcome of a policy step that has been reassigned because it had an error provisioning."""
    restart_action: NotRequired[Nullable[RestartActionTypedDict]]
    r"""The restart action describes the outcome of policy steps for when the task was restarted. This can be applied to multiple steps since restart skips all pending next steps."""
    state: NotRequired[ApprovalInstanceState]
    r"""The state of the approval instance"""
    

class ApprovalInstance(BaseModel):
    r"""The approval instance object describes the way a policy step should be approved as well as its outcomes and state.

    This message contains a oneof named outcome. Only a single field of the following list may be set at a time:
    - approved
    - denied
    - reassigned
    - restarted
    - reassignedByError

    """
    
    approval: OptionalNullable[Approval] = UNSET
    r"""The Approval message.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
    - users
    - manager
    - appOwners
    - group
    - self
    - entitlementOwners
    - expression
    - webhook

    """
    approved_action: Annotated[OptionalNullable[ApprovedAction], pydantic.Field(alias="approved")] = UNSET
    r"""The approved action indicates that the approvalinstance had an outcome of approved."""
    denied_action: Annotated[OptionalNullable[DeniedAction], pydantic.Field(alias="denied")] = UNSET
    r"""The denied action indicates that the c1.api.policy.v1.ApprovalInstance had an outcome of denied."""
    reassigned_action: Annotated[OptionalNullable[ReassignedAction], pydantic.Field(alias="reassigned")] = UNSET
    r"""The ReassignedAction object describes the outcome of a policy step that has been reassigned."""
    reassigned_by_error_action: Annotated[OptionalNullable[ReassignedByErrorAction], pydantic.Field(alias="reassignedByError")] = UNSET
    r"""The ReassignedByErrorAction object describes the outcome of a policy step that has been reassigned because it had an error provisioning."""
    restart_action: Annotated[OptionalNullable[RestartAction], pydantic.Field(alias="restarted")] = UNSET
    r"""The restart action describes the outcome of policy steps for when the task was restarted. This can be applied to multiple steps since restart skips all pending next steps."""
    state: Optional[ApprovalInstanceState] = None
    r"""The state of the approval instance"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["Approval", "ApprovedAction", "DeniedAction", "ReassignedAction", "ReassignedByErrorAction", "RestartAction", "state"]
        nullable_fields = ["Approval", "ApprovedAction", "DeniedAction", "ReassignedAction", "ReassignedByErrorAction", "RestartAction"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        
