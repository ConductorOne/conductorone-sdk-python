"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UserAttributeMappingSourceTypedDict(TypedDict):
    r"""The UserAttributeMappingSource message."""
    
    app_id: NotRequired[str]
    r"""The appId field."""
    app_user_id: NotRequired[str]
    r"""The appUserId field."""
    app_user_profile_attribute_key: NotRequired[str]
    r"""The appUserProfileAttributeKey field."""
    user_attribute_mapping_id: NotRequired[str]
    r"""The userAttributeMappingId field."""
    value: NotRequired[str]
    r"""The value field."""
    

class UserAttributeMappingSource(BaseModel):
    r"""The UserAttributeMappingSource message."""
    
    app_id: Annotated[Optional[str], pydantic.Field(alias="appId")] = None
    r"""The appId field."""
    app_user_id: Annotated[Optional[str], pydantic.Field(alias="appUserId")] = None
    r"""The appUserId field."""
    app_user_profile_attribute_key: Annotated[Optional[str], pydantic.Field(alias="appUserProfileAttributeKey")] = None
    r"""The appUserProfileAttributeKey field."""
    user_attribute_mapping_id: Annotated[Optional[str], pydantic.Field(alias="userAttributeMappingId")] = None
    r"""The userAttributeMappingId field."""
    value: Optional[str] = None
    r"""The value field."""
    
