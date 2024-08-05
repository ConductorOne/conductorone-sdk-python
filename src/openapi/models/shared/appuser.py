"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appuserstatus import AppUserStatus, AppUserStatusTypedDict
from .appuserstatus_input import AppUserStatusInput, AppUserStatusInputTypedDict
from datetime import datetime
from enum import Enum
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppUserType(str, Enum):
    r"""The appplication user type. Type can be user, system or service."""
    APP_USER_TYPE_UNSPECIFIED = "APP_USER_TYPE_UNSPECIFIED"
    APP_USER_TYPE_USER = "APP_USER_TYPE_USER"
    APP_USER_TYPE_SERVICE_ACCOUNT = "APP_USER_TYPE_SERVICE_ACCOUNT"
    APP_USER_TYPE_SYSTEM_ACCOUNT = "APP_USER_TYPE_SYSTEM_ACCOUNT"

class AppUserTypedDict(TypedDict):
    r"""Application User that represents an account in the application."""
    
    app_user_status: NotRequired[AppUserStatusTypedDict]
    r"""The satus of the applicaiton user."""
    app_id: NotRequired[str]
    r"""The ID of the application."""
    app_user_type: NotRequired[AppUserType]
    r"""The appplication user type. Type can be user, system or service."""
    created_at: NotRequired[datetime]
    deleted_at: NotRequired[datetime]
    display_name: NotRequired[str]
    r"""The display name of the application user."""
    email: NotRequired[str]
    r"""The email field of the application user."""
    emails: NotRequired[Nullable[List[str]]]
    r"""The emails field of the application user."""
    id: NotRequired[str]
    r"""A unique idenditfier of the application user."""
    identity_user_id: NotRequired[str]
    r"""The conductor one user ID of the account owner."""
    profile: NotRequired[Dict[str, Any]]
    updated_at: NotRequired[datetime]
    username: NotRequired[str]
    r"""The username field of the application user."""
    usernames: NotRequired[Nullable[List[str]]]
    r"""The usernames field of the application user."""
    

class AppUser(BaseModel):
    r"""Application User that represents an account in the application."""
    
    app_user_status: Annotated[Optional[AppUserStatus], pydantic.Field(alias="status")] = None
    r"""The satus of the applicaiton user."""
    app_id: Annotated[Optional[str], pydantic.Field(alias="appId")] = None
    r"""The ID of the application."""
    app_user_type: Annotated[Optional[AppUserType], pydantic.Field(alias="appUserType")] = None
    r"""The appplication user type. Type can be user, system or service."""
    created_at: Annotated[Optional[datetime], pydantic.Field(alias="createdAt")] = None
    deleted_at: Annotated[Optional[datetime], pydantic.Field(alias="deletedAt")] = None
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The display name of the application user."""
    email: Optional[str] = None
    r"""The email field of the application user."""
    emails: OptionalNullable[List[str]] = UNSET
    r"""The emails field of the application user."""
    id: Optional[str] = None
    r"""A unique idenditfier of the application user."""
    identity_user_id: Annotated[Optional[str], pydantic.Field(alias="identityUserId")] = None
    r"""The conductor one user ID of the account owner."""
    profile: Optional[Dict[str, Any]] = None
    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
    username: Optional[str] = None
    r"""The username field of the application user."""
    usernames: OptionalNullable[List[str]] = UNSET
    r"""The usernames field of the application user."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["AppUserStatus", "appId", "appUserType", "createdAt", "deletedAt", "displayName", "email", "emails", "id", "identityUserId", "profile", "updatedAt", "username", "usernames"]
        nullable_fields = ["emails", "usernames"]
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
        

class AppUserInputTypedDict(TypedDict):
    r"""Application User that represents an account in the application."""
    
    app_user_status: NotRequired[AppUserStatusInputTypedDict]
    r"""The satus of the applicaiton user."""
    app_user_type: NotRequired[AppUserType]
    r"""The appplication user type. Type can be user, system or service."""
    

class AppUserInput(BaseModel):
    r"""Application User that represents an account in the application."""
    
    app_user_status: Annotated[Optional[AppUserStatusInput], pydantic.Field(alias="status")] = None
    r"""The satus of the applicaiton user."""
    app_user_type: Annotated[Optional[AppUserType], pydantic.Field(alias="appUserType")] = None
    r"""The appplication user type. Type can be user, system or service."""
    