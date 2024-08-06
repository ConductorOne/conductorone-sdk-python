"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .user import User, UserTypedDict
from datetime import datetime
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from sdk.utils import serialize_int, validate_int
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class IdentityMatching(str, Enum):
    r"""The identityMatching field."""
    APP_USER_IDENTITY_MATCHING_UNSPECIFIED = "APP_USER_IDENTITY_MATCHING_UNSPECIFIED"
    APP_USER_IDENTITY_MATCHING_STRICT = "APP_USER_IDENTITY_MATCHING_STRICT"
    APP_USER_IDENTITY_MATCHING_DISPLAY_NAME = "APP_USER_IDENTITY_MATCHING_DISPLAY_NAME"

class AppTypedDict(TypedDict):
    r"""The App object provides all of the details for an app, as well as some configuration."""
    
    app_account_id: NotRequired[str]
    r"""The ID of the Account named by AccountName."""
    app_account_name: NotRequired[str]
    r"""The AccountName of the app. For example, AWS is AccountID, Github is Org Name, and Okta is Okta Subdomain."""
    app_owners: NotRequired[Nullable[List[UserTypedDict]]]
    r"""The owners of the app."""
    certify_policy_id: NotRequired[str]
    r"""The ID of the Certify Policy associated with this App."""
    created_at: NotRequired[datetime]
    deleted_at: NotRequired[datetime]
    description: NotRequired[str]
    r"""The app's description."""
    display_name: NotRequired[str]
    r"""The app's display name."""
    field_mask: NotRequired[Nullable[str]]
    grant_policy_id: NotRequired[str]
    r"""The ID of the Grant Policy associated with this App."""
    icon_url: NotRequired[str]
    r"""The URL of an icon to display for the app."""
    id: NotRequired[str]
    r"""The ID of the app."""
    identity_matching: NotRequired[IdentityMatching]
    r"""The identityMatching field."""
    is_directory: NotRequired[bool]
    r"""Specifies if the app is a directory."""
    logo_uri: NotRequired[str]
    r"""The URL of a logo to display for the app."""
    monthly_cost_usd: NotRequired[int]
    r"""The cost of an app per-seat, so that total cost can be calculated by the grant count."""
    parent_app_id: NotRequired[str]
    r"""The ID of the app that created this app, if any."""
    revoke_policy_id: NotRequired[str]
    r"""The ID of the Revoke Policy associated with this App."""
    updated_at: NotRequired[datetime]
    user_count: NotRequired[int]
    r"""The number of users with grants to this app."""
    

class App(BaseModel):
    r"""The App object provides all of the details for an app, as well as some configuration."""
    
    app_account_id: Annotated[Optional[str], pydantic.Field(alias="appAccountId")] = None
    r"""The ID of the Account named by AccountName."""
    app_account_name: Annotated[Optional[str], pydantic.Field(alias="appAccountName")] = None
    r"""The AccountName of the app. For example, AWS is AccountID, Github is Org Name, and Okta is Okta Subdomain."""
    app_owners: Annotated[OptionalNullable[List[User]], pydantic.Field(alias="appOwners")] = UNSET
    r"""The owners of the app."""
    certify_policy_id: Annotated[Optional[str], pydantic.Field(alias="certifyPolicyId")] = None
    r"""The ID of the Certify Policy associated with this App."""
    created_at: Annotated[Optional[datetime], pydantic.Field(alias="createdAt")] = None
    deleted_at: Annotated[Optional[datetime], pydantic.Field(alias="deletedAt")] = None
    description: Optional[str] = None
    r"""The app's description."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The app's display name."""
    field_mask: Annotated[OptionalNullable[str], pydantic.Field(alias="fieldMask")] = UNSET
    grant_policy_id: Annotated[Optional[str], pydantic.Field(alias="grantPolicyId")] = None
    r"""The ID of the Grant Policy associated with this App."""
    icon_url: Annotated[Optional[str], pydantic.Field(alias="iconUrl")] = None
    r"""The URL of an icon to display for the app."""
    id: Optional[str] = None
    r"""The ID of the app."""
    identity_matching: Annotated[Optional[IdentityMatching], pydantic.Field(alias="identityMatching")] = None
    r"""The identityMatching field."""
    is_directory: Annotated[Optional[bool], pydantic.Field(alias="isDirectory")] = None
    r"""Specifies if the app is a directory."""
    logo_uri: Annotated[Optional[str], pydantic.Field(alias="logoUri")] = None
    r"""The URL of a logo to display for the app."""
    monthly_cost_usd: Annotated[Optional[int], pydantic.Field(alias="monthlyCostUsd")] = None
    r"""The cost of an app per-seat, so that total cost can be calculated by the grant count."""
    parent_app_id: Annotated[Optional[str], pydantic.Field(alias="parentAppId")] = None
    r"""The ID of the app that created this app, if any."""
    revoke_policy_id: Annotated[Optional[str], pydantic.Field(alias="revokePolicyId")] = None
    r"""The ID of the Revoke Policy associated with this App."""
    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
    user_count: Annotated[Annotated[Optional[int], BeforeValidator(validate_int), PlainSerializer(serialize_int(True))], pydantic.Field(alias="userCount")] = None
    r"""The number of users with grants to this app."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["appAccountId", "appAccountName", "appOwners", "certifyPolicyId", "createdAt", "deletedAt", "description", "displayName", "fieldMask", "grantPolicyId", "iconUrl", "id", "identityMatching", "isDirectory", "logoUri", "monthlyCostUsd", "parentAppId", "revokePolicyId", "updatedAt", "userCount"]
        nullable_fields = ["appOwners", "fieldMask"]
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
        

class AppInputTypedDict(TypedDict):
    r"""The App object provides all of the details for an app, as well as some configuration."""
    
    certify_policy_id: NotRequired[str]
    r"""The ID of the Certify Policy associated with this App."""
    description: NotRequired[str]
    r"""The app's description."""
    display_name: NotRequired[str]
    r"""The app's display name."""
    grant_policy_id: NotRequired[str]
    r"""The ID of the Grant Policy associated with this App."""
    icon_url: NotRequired[str]
    r"""The URL of an icon to display for the app."""
    identity_matching: NotRequired[IdentityMatching]
    r"""The identityMatching field."""
    monthly_cost_usd: NotRequired[int]
    r"""The cost of an app per-seat, so that total cost can be calculated by the grant count."""
    revoke_policy_id: NotRequired[str]
    r"""The ID of the Revoke Policy associated with this App."""
    

class AppInput(BaseModel):
    r"""The App object provides all of the details for an app, as well as some configuration."""
    
    certify_policy_id: Annotated[Optional[str], pydantic.Field(alias="certifyPolicyId")] = None
    r"""The ID of the Certify Policy associated with this App."""
    description: Optional[str] = None
    r"""The app's description."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The app's display name."""
    grant_policy_id: Annotated[Optional[str], pydantic.Field(alias="grantPolicyId")] = None
    r"""The ID of the Grant Policy associated with this App."""
    icon_url: Annotated[Optional[str], pydantic.Field(alias="iconUrl")] = None
    r"""The URL of an icon to display for the app."""
    identity_matching: Annotated[Optional[IdentityMatching], pydantic.Field(alias="identityMatching")] = None
    r"""The identityMatching field."""
    monthly_cost_usd: Annotated[Optional[int], pydantic.Field(alias="monthlyCostUsd")] = None
    r"""The cost of an app per-seat, so that total cost can be calculated by the grant count."""
    revoke_policy_id: Annotated[Optional[str], pydantic.Field(alias="revokePolicyId")] = None
    r"""The ID of the Revoke Policy associated with this App."""
    
