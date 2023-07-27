"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import taskexpandmask as shared_taskexpandmask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskServiceCreateGrantRequest:
    r"""Create a grant task."""
    app_entitlement_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementId') }})
    r"""The ID of the app entitlement to grant access to."""
    app_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId') }})
    r"""The ID of the app that is associated with the entitlement."""
    app_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app user to grant access for. This field and identityUserId cannot both be set for a given request."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the request."""
    emergency_access: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emergencyAccess'), 'exclude': lambda f: f is None }})
    r"""Boolean stating whether or not the task is marked as emergency access."""
    grant_duration: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantDuration'), 'exclude': lambda f: f is None }})
    identity_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the user associated with the app user we are granting access for. This field cannot be set if appUserID is also set."""
    task_expand_mask: Optional[shared_taskexpandmask.TaskExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    

