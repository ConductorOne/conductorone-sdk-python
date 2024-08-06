"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .policypostactions import PolicyPostActions, PolicyPostActionsTypedDict
from .policysteps import PolicySteps, PolicyStepsTypedDict
from .rule import Rule, RuleTypedDict
from enum import Enum
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PolicyType(str, Enum):
    r"""The enum of the policy type."""
    POLICY_TYPE_UNSPECIFIED = "POLICY_TYPE_UNSPECIFIED"
    POLICY_TYPE_GRANT = "POLICY_TYPE_GRANT"
    POLICY_TYPE_REVOKE = "POLICY_TYPE_REVOKE"
    POLICY_TYPE_CERTIFY = "POLICY_TYPE_CERTIFY"
    POLICY_TYPE_ACCESS_REQUEST = "POLICY_TYPE_ACCESS_REQUEST"
    POLICY_TYPE_PROVISION = "POLICY_TYPE_PROVISION"

class CreatePolicyRequestTypedDict(TypedDict):
    r"""The CreatePolicyRequest message is used to create a new policy."""
    
    description: NotRequired[str]
    r"""The description of the new policy."""
    display_name: NotRequired[str]
    r"""The display name of the new policy."""
    policy_steps: NotRequired[Dict[str, PolicyStepsTypedDict]]
    r"""The map of policy type to policy steps. The key is the stringified version of the enum. See other policies for examples."""
    policy_type: NotRequired[PolicyType]
    r"""The enum of the policy type."""
    post_actions: NotRequired[Nullable[List[PolicyPostActionsTypedDict]]]
    r"""Actions to occur after a policy finishes. As of now this is only valid on a certify policy to remediate a denied certification immediately."""
    reassign_tasks_to_delegates: NotRequired[bool]
    r"""Allows reassigning tasks to delegates."""
    rules: NotRequired[Nullable[List[RuleTypedDict]]]
    r"""The rules field."""
    

class CreatePolicyRequest(BaseModel):
    r"""The CreatePolicyRequest message is used to create a new policy."""
    
    description: Optional[str] = None
    r"""The description of the new policy."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The display name of the new policy."""
    policy_steps: Annotated[Optional[Dict[str, PolicySteps]], pydantic.Field(alias="policySteps")] = None
    r"""The map of policy type to policy steps. The key is the stringified version of the enum. See other policies for examples."""
    policy_type: Annotated[Optional[PolicyType], pydantic.Field(alias="policyType")] = None
    r"""The enum of the policy type."""
    post_actions: Annotated[OptionalNullable[List[PolicyPostActions]], pydantic.Field(alias="postActions")] = UNSET
    r"""Actions to occur after a policy finishes. As of now this is only valid on a certify policy to remediate a denied certification immediately."""
    reassign_tasks_to_delegates: Annotated[Optional[bool], pydantic.Field(alias="reassignTasksToDelegates")] = None
    r"""Allows reassigning tasks to delegates."""
    rules: OptionalNullable[List[Rule]] = UNSET
    r"""The rules field."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "displayName", "policySteps", "policyType", "postActions", "reassignTasksToDelegates", "rules"]
        nullable_fields = ["postActions", "rules"]
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
        
