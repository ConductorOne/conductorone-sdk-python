"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .user import User
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import List, Optional


class IdentityMatching(str, Enum):
    r"""The identityMatching field."""
    APP_USER_IDENTITY_MATCHING_UNSPECIFIED = 'APP_USER_IDENTITY_MATCHING_UNSPECIFIED'
    APP_USER_IDENTITY_MATCHING_STRICT = 'APP_USER_IDENTITY_MATCHING_STRICT'
    APP_USER_IDENTITY_MATCHING_DISPLAY_NAME = 'APP_USER_IDENTITY_MATCHING_DISPLAY_NAME'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class App:
    r"""The App object provides all of the details for an app, as well as some configuration."""
    UNSET='__SPEAKEASY_UNSET__'
    app_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appAccountId'), 'exclude': lambda f: f is None }})
    r"""The ID of the Account named by AccountName."""
    app_account_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appAccountName'), 'exclude': lambda f: f is None }})
    r"""The AccountName of the app. For example, AWS is AccountID, Github is Org Name, and Okta is Okta Subdomain."""
    app_owners: Optional[List[User]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appOwners'), 'exclude': lambda f: f is App.UNSET }})
    r"""The owners of the app."""
    certify_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certifyPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the Certify Policy associated with this App."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The app's description."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The app's display name."""
    field_mask: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fieldMask'), 'exclude': lambda f: f is App.UNSET }})
    grant_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the Grant Policy associated with this App."""
    icon_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iconUrl'), 'exclude': lambda f: f is None }})
    r"""The URL of an icon to display for the app."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The ID of the app."""
    identity_matching: Optional[IdentityMatching] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityMatching'), 'exclude': lambda f: f is None }})
    r"""The identityMatching field."""
    is_directory: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDirectory'), 'exclude': lambda f: f is None }})
    r"""Specifies if the app is a directory."""
    logo_uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logoUri'), 'exclude': lambda f: f is None }})
    r"""The URL of a logo to display for the app."""
    monthly_cost_usd: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monthlyCostUsd'), 'exclude': lambda f: f is None }})
    r"""The cost of an app per-seat, so that total cost can be calculated by the grant count."""
    parent_app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentAppId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app that created this app, if any."""
    revoke_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revokePolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the Revoke Policy associated with this App."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    user_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userCount'), 'encoder': utils.integerstrencoder(True), 'decoder': utils.integerstrdecoder, 'exclude': lambda f: f is None }})
    r"""The number of users with grants to this app."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppInput:
    r"""The App object provides all of the details for an app, as well as some configuration."""
    certify_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certifyPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the Certify Policy associated with this App."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The app's description."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The app's display name."""
    grant_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the Grant Policy associated with this App."""
    icon_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iconUrl'), 'exclude': lambda f: f is None }})
    r"""The URL of an icon to display for the app."""
    identity_matching: Optional[IdentityMatching] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityMatching'), 'exclude': lambda f: f is None }})
    r"""The identityMatching field."""
    monthly_cost_usd: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('monthlyCostUsd'), 'exclude': lambda f: f is None }})
    r"""The cost of an app per-seat, so that total cost can be calculated by the grant count."""
    revoke_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revokePolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the Revoke Policy associated with this App."""
    

