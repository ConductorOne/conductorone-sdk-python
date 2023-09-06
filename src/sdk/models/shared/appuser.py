"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import appuserstatus as shared_appuserstatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any, Optional

class AppUserAppUserType(str, Enum):
    r"""The appplication user type. Type can be user, system or service."""
    APP_USER_TYPE_UNSPECIFIED = 'APP_USER_TYPE_UNSPECIFIED'
    APP_USER_TYPE_USER = 'APP_USER_TYPE_USER'
    APP_USER_TYPE_SERVICE_ACCOUNT = 'APP_USER_TYPE_SERVICE_ACCOUNT'
    APP_USER_TYPE_SYSTEM_ACCOUNT = 'APP_USER_TYPE_SYSTEM_ACCOUNT'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppUserInput:
    r"""Application User that represents an account in the application."""
    app_user_status: Optional[shared_appuserstatus.AppUserStatusInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The satus of the applicaiton user."""
    app_user_type: Optional[AppUserAppUserType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserType'), 'exclude': lambda f: f is None }})
    r"""The appplication user type. Type can be user, system or service."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppUser:
    r"""Application User that represents an account in the application."""
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The ID of the application."""
    app_user_status: Optional[shared_appuserstatus.AppUserStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The satus of the applicaiton user."""
    app_user_type: Optional[AppUserAppUserType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserType'), 'exclude': lambda f: f is None }})
    r"""The appplication user type. Type can be user, system or service."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the application user."""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""The email field of the application user."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""A unique idenditfier of the application user."""
    identity_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityUserId'), 'exclude': lambda f: f is None }})
    r"""The conductor one user ID of the account owner."""
    profile: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profile'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

