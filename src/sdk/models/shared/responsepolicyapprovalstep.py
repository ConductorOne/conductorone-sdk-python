"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .responsepolicyapprovalreplacepolicy import ResponsePolicyApprovalReplacePolicy, ResponsePolicyApprovalReplacePolicyTypedDict
from .responsepolicyapprovalstepapprove import ResponsePolicyApprovalStepApprove, ResponsePolicyApprovalStepApproveTypedDict
from .responsepolicyapprovalstepdeny import ResponsePolicyApprovalStepDeny, ResponsePolicyApprovalStepDenyTypedDict
from .responsepolicyapprovalstepreassign import ResponsePolicyApprovalStepReassign, ResponsePolicyApprovalStepReassignTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ResponsePolicyApprovalStepTypedDict(TypedDict):
    r"""The ResponsePolicyApprovalStep message.

    This message contains a oneof named action. Only a single field of the following list may be set at a time:
    - approve
    - deny
    - reassign
    - replacePolicy

    """
    
    response_policy_approval_replace_policy: NotRequired[Nullable[ResponsePolicyApprovalReplacePolicyTypedDict]]
    r"""The ResponsePolicyApprovalReplacePolicy message."""
    response_policy_approval_step_approve: NotRequired[Nullable[ResponsePolicyApprovalStepApproveTypedDict]]
    r"""The ResponsePolicyApprovalStepApprove message."""
    response_policy_approval_step_deny: NotRequired[Nullable[ResponsePolicyApprovalStepDenyTypedDict]]
    r"""The ResponsePolicyApprovalStepDeny message."""
    response_policy_approval_step_reassign: NotRequired[Nullable[ResponsePolicyApprovalStepReassignTypedDict]]
    r"""The ResponsePolicyApprovalStepReassign message."""
    version: NotRequired[str]
    r"""version contains the constant value \"v1\". Future versions of the Webhook Response
    will use a different string.
    """
    

class ResponsePolicyApprovalStep(BaseModel):
    r"""The ResponsePolicyApprovalStep message.

    This message contains a oneof named action. Only a single field of the following list may be set at a time:
    - approve
    - deny
    - reassign
    - replacePolicy

    """
    
    response_policy_approval_replace_policy: Annotated[OptionalNullable[ResponsePolicyApprovalReplacePolicy], pydantic.Field(alias="replacePolicy")] = UNSET
    r"""The ResponsePolicyApprovalReplacePolicy message."""
    response_policy_approval_step_approve: Annotated[OptionalNullable[ResponsePolicyApprovalStepApprove], pydantic.Field(alias="approve")] = UNSET
    r"""The ResponsePolicyApprovalStepApprove message."""
    response_policy_approval_step_deny: Annotated[OptionalNullable[ResponsePolicyApprovalStepDeny], pydantic.Field(alias="deny")] = UNSET
    r"""The ResponsePolicyApprovalStepDeny message."""
    response_policy_approval_step_reassign: Annotated[OptionalNullable[ResponsePolicyApprovalStepReassign], pydantic.Field(alias="reassign")] = UNSET
    r"""The ResponsePolicyApprovalStepReassign message."""
    version: Optional[str] = None
    r"""version contains the constant value \"v1\". Future versions of the Webhook Response
    will use a different string.
    """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ResponsePolicyApprovalReplacePolicy", "ResponsePolicyApprovalStepApprove", "ResponsePolicyApprovalStepDeny", "ResponsePolicyApprovalStepReassign", "version"]
        nullable_fields = ["ResponsePolicyApprovalReplacePolicy", "ResponsePolicyApprovalStepApprove", "ResponsePolicyApprovalStepDeny", "ResponsePolicyApprovalStepReassign"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
