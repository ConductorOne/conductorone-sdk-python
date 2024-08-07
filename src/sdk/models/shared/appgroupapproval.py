"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppGroupApprovalTypedDict(TypedDict):
    r"""The AppGroupApproval object provides the configuration for setting a group as the approvers of an approval policy step."""
    
    allow_self_approval: NotRequired[bool]
    r"""Configuration to allow self approval if the target user is a member of the group during this step."""
    app_group_id: NotRequired[str]
    r"""The ID of the group specified for approval."""
    app_id: NotRequired[str]
    r"""The ID of the app that contains the group specified for approval."""
    fallback: NotRequired[bool]
    r"""Configuration to allow a fallback if the group is empty."""
    fallback_user_ids: NotRequired[Nullable[List[str]]]
    r"""Configuration to specific which users to fallback to if fallback is enabled and the group is empty."""
    

class AppGroupApproval(BaseModel):
    r"""The AppGroupApproval object provides the configuration for setting a group as the approvers of an approval policy step."""
    
    allow_self_approval: Annotated[Optional[bool], pydantic.Field(alias="allowSelfApproval")] = None
    r"""Configuration to allow self approval if the target user is a member of the group during this step."""
    app_group_id: Annotated[Optional[str], pydantic.Field(alias="appGroupId")] = None
    r"""The ID of the group specified for approval."""
    app_id: Annotated[Optional[str], pydantic.Field(alias="appId")] = None
    r"""The ID of the app that contains the group specified for approval."""
    fallback: Optional[bool] = None
    r"""Configuration to allow a fallback if the group is empty."""
    fallback_user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="fallbackUserIds")] = UNSET
    r"""Configuration to specific which users to fallback to if fallback is enabled and the group is empty."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["allowSelfApproval", "appGroupId", "appId", "fallback", "fallbackUserIds"]
        nullable_fields = ["fallbackUserIds"]
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
        
