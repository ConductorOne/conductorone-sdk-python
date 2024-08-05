"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SelfApprovalTypedDict(TypedDict):
    r"""The self approval object describes the configuration of a policy step that needs to be approved by the target of the request."""
    
    assigned_user_ids: NotRequired[Nullable[List[str]]]
    r"""The array of users determined to be themselves during approval. This should only ever be one person, but is saved because it may change if the owner of an app user changes while the ticket is open."""
    fallback: NotRequired[bool]
    r"""Configuration to allow a fallback if the identity user of the target app user cannot be determined."""
    fallback_user_ids: NotRequired[Nullable[List[str]]]
    r"""Configuration to specific which users to fallback to if fallback is enabled and the identity user of the target app user cannot be determined."""
    

class SelfApproval(BaseModel):
    r"""The self approval object describes the configuration of a policy step that needs to be approved by the target of the request."""
    
    assigned_user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="assignedUserIds")] = UNSET
    r"""The array of users determined to be themselves during approval. This should only ever be one person, but is saved because it may change if the owner of an app user changes while the ticket is open."""
    fallback: Optional[bool] = None
    r"""Configuration to allow a fallback if the identity user of the target app user cannot be determined."""
    fallback_user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="fallbackUserIds")] = UNSET
    r"""Configuration to specific which users to fallback to if fallback is enabled and the identity user of the target app user cannot be determined."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["assignedUserIds", "fallback", "fallbackUserIds"]
        nullable_fields = ["assignedUserIds", "fallbackUserIds"]
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
        
