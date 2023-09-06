"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PersonalClientServiceCreateRequest:
    r"""The PersonalClientServiceCreateRequest message contains the fields for creating a new personal client."""
    allow_source_cidr: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowSourceCidr'), 'exclude': lambda f: f is None }})
    r"""A list of CIDRs to restrict this credential to."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name for the new personal client."""
    expires: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires'), 'exclude': lambda f: f is None }})
    scoped_roles: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scopedRoles'), 'exclude': lambda f: f is None }})
    r"""The list of roles to restrict the credential to."""
    

