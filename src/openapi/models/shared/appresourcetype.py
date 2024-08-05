"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppResourceTypeTypedDict(TypedDict):
    r"""The AppResourceType is referenced by an app entitlement defining its resource types. Commonly things like Group or Role."""
    
    app_id: NotRequired[str]
    r"""The ID of the app that is associated with the app resource type"""
    created_at: NotRequired[datetime]
    deleted_at: NotRequired[datetime]
    display_name: NotRequired[str]
    r"""The display name of the app resource type."""
    id: NotRequired[str]
    r"""The unique ID for the app resource type."""
    updated_at: NotRequired[datetime]
    

class AppResourceType(BaseModel):
    r"""The AppResourceType is referenced by an app entitlement defining its resource types. Commonly things like Group or Role."""
    
    app_id: Annotated[Optional[str], pydantic.Field(alias="appId")] = None
    r"""The ID of the app that is associated with the app resource type"""
    created_at: Annotated[Optional[datetime], pydantic.Field(alias="createdAt")] = None
    deleted_at: Annotated[Optional[datetime], pydantic.Field(alias="deletedAt")] = None
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The display name of the app resource type."""
    id: Optional[str] = None
    r"""The unique ID for the app resource type."""
    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
    