"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accept import Accept, AcceptTypedDict
from .approval import Approval, ApprovalTypedDict
from .provision import Provision, ProvisionTypedDict
from .reject import Reject, RejectTypedDict
from .wait import Wait, WaitTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class PolicyStepTypedDict(TypedDict):
    r"""The PolicyStep message.

    This message contains a oneof named step. Only a single field of the following list may be set at a time:
    - approval
    - provision
    - accept
    - reject
    - wait

    """
    
    accept: NotRequired[Nullable[AcceptTypedDict]]
    r"""This policy step indicates that a ticket should have an approved outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
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
    provision: NotRequired[Nullable[ProvisionTypedDict]]
    r"""The provision step references a provision policy for this step."""
    reject: NotRequired[Nullable[RejectTypedDict]]
    r"""This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    wait: NotRequired[Nullable[WaitTypedDict]]
    r"""Define a Wait step for a policy to wait on a condition to be met.

    This message contains a oneof named until. Only a single field of the following list may be set at a time:
    - condition

    """
    

class PolicyStep(BaseModel):
    r"""The PolicyStep message.

    This message contains a oneof named step. Only a single field of the following list may be set at a time:
    - approval
    - provision
    - accept
    - reject
    - wait

    """
    
    accept: OptionalNullable[Accept] = UNSET
    r"""This policy step indicates that a ticket should have an approved outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
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
    provision: OptionalNullable[Provision] = UNSET
    r"""The provision step references a provision policy for this step."""
    reject: OptionalNullable[Reject] = UNSET
    r"""This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    wait: OptionalNullable[Wait] = UNSET
    r"""Define a Wait step for a policy to wait on a condition to be met.

    This message contains a oneof named until. Only a single field of the following list may be set at a time:
    - condition

    """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["Accept", "Approval", "Provision", "Reject", "Wait"]
        nullable_fields = ["Accept", "Approval", "Provision", "Reject", "Wait"]
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
        