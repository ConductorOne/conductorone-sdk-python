"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UserApprovalTypedDict(TypedDict):
    r"""The user approval object describes the approval configuration of a policy step that needs to be approved by a specific list of users."""
    
    allow_self_approval: NotRequired[bool]
    r"""Configuration to allow self approval of if the user is specified and also the target of the ticket."""
    user_ids: NotRequired[Nullable[List[str]]]
    r"""Array of users configured for approval."""
    

class UserApproval(BaseModel):
    r"""The user approval object describes the approval configuration of a policy step that needs to be approved by a specific list of users."""
    
    allow_self_approval: Annotated[Optional[bool], pydantic.Field(alias="allowSelfApproval")] = None
    r"""Configuration to allow self approval of if the user is specified and also the target of the ticket."""
    user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="userIds")] = UNSET
    r"""Array of users configured for approval."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["allowSelfApproval", "userIds"]
        nullable_fields = ["userIds"]
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
        
