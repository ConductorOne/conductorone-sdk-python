"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .policy import Policy, PolicyTypedDict
from .policystep import PolicyStep, PolicyStepTypedDict
from .policystepinstance import PolicyStepInstance, PolicyStepInstanceTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PolicyInstanceTypedDict(TypedDict):
    r"""A policy instance is an object that contains a reference to the policy it was created from, the currently executing step, the next steps, and the history of previously completed steps."""
    
    policy: NotRequired[PolicyTypedDict]
    r"""A policy describes the behavior of the ConductorOne system when processing a task. You can describe the type, approvers, fallback behavior, and escalation processes."""
    policy_step_instance: NotRequired[PolicyStepInstanceTypedDict]
    r"""The policy step instance includes a reference to an instance of a policy step that tracks state and has a unique ID.

    This message contains a oneof named instance. Only a single field of the following list may be set at a time:
    - approval
    - provision
    - accept
    - reject
    - wait

    """
    history: NotRequired[Nullable[List[PolicyStepInstanceTypedDict]]]
    r"""An array of steps that were previously processed by the ticket with their outcomes set, in order."""
    next: NotRequired[Nullable[List[PolicyStepTypedDict]]]
    r"""An array of steps that will be processed by the ticket, in order."""
    

class PolicyInstance(BaseModel):
    r"""A policy instance is an object that contains a reference to the policy it was created from, the currently executing step, the next steps, and the history of previously completed steps."""
    
    policy: Optional[Policy] = None
    r"""A policy describes the behavior of the ConductorOne system when processing a task. You can describe the type, approvers, fallback behavior, and escalation processes."""
    policy_step_instance: Annotated[Optional[PolicyStepInstance], pydantic.Field(alias="current")] = None
    r"""The policy step instance includes a reference to an instance of a policy step that tracks state and has a unique ID.

    This message contains a oneof named instance. Only a single field of the following list may be set at a time:
    - approval
    - provision
    - accept
    - reject
    - wait

    """
    history: OptionalNullable[List[PolicyStepInstance]] = UNSET
    r"""An array of steps that were previously processed by the ticket with their outcomes set, in order."""
    next: OptionalNullable[List[PolicyStep]] = UNSET
    r"""An array of steps that will be processed by the ticket, in order."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["Policy", "PolicyStepInstance", "history", "next"]
        nullable_fields = ["history", "next"]
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
        
