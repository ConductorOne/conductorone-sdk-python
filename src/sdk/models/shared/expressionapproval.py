"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ExpressionApprovalTypedDict(TypedDict):
    r"""The ExpressionApproval message."""
    
    allow_self_approval: NotRequired[bool]
    r"""Configuration to allow self approval of if the user is specified and also the target of the ticket."""
    assigned_user_ids: NotRequired[Nullable[List[str]]]
    r"""The assignedUserIds field."""
    expressions: NotRequired[Nullable[List[str]]]
    r"""Array of dynamic expressions to determine the approvers.  The first expression to return a non-empty list of users will be used."""
    fallback: NotRequired[bool]
    r"""Configuration to allow a fallback if the expression does not return a valid list of users."""
    fallback_user_ids: NotRequired[Nullable[List[str]]]
    r"""Configuration to specific which users to fallback to if and the expression does not return a valid list of users."""
    

class ExpressionApproval(BaseModel):
    r"""The ExpressionApproval message."""
    
    allow_self_approval: Annotated[Optional[bool], pydantic.Field(alias="allowSelfApproval")] = None
    r"""Configuration to allow self approval of if the user is specified and also the target of the ticket."""
    assigned_user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="assignedUserIds")] = UNSET
    r"""The assignedUserIds field."""
    expressions: OptionalNullable[List[str]] = UNSET
    r"""Array of dynamic expressions to determine the approvers.  The first expression to return a non-empty list of users will be used."""
    fallback: Optional[bool] = None
    r"""Configuration to allow a fallback if the expression does not return a valid list of users."""
    fallback_user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="fallbackUserIds")] = UNSET
    r"""Configuration to specific which users to fallback to if and the expression does not return a valid list of users."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["allowSelfApproval", "assignedUserIds", "expressions", "fallback", "fallbackUserIds"]
        nullable_fields = ["assignedUserIds", "expressions", "fallbackUserIds"]
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
        
