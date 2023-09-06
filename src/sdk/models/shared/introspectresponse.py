"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class IntrospectResponse:
    r"""IntrospectResponse contains information about the current user who is authenticated."""
    features: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('features'), 'exclude': lambda f: f is None }})
    r"""The list of feature flags enabled for the tenant the logged in user belongs to."""
    permissions: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('permissions'), 'exclude': lambda f: f is None }})
    r"""The list of permissions that the current logged in user has."""
    principle_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('principleId'), 'exclude': lambda f: f is None }})
    r"""The principleID of the current logged in user."""
    roles: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('roles'), 'exclude': lambda f: f is None }})
    r"""The list of roles that the current logged in user has."""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId'), 'exclude': lambda f: f is None }})
    r"""The userID of the current logged in user."""
    

