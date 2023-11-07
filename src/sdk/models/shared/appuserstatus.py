"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class AppUserStatusInput:
    r"""The satus of the applicaiton user."""
    


class Status(str, Enum):
    r"""The application user status field."""
    STATUS_UNSPECIFIED = 'STATUS_UNSPECIFIED'
    STATUS_ENABLED = 'STATUS_ENABLED'
    STATUS_DISABLED = 'STATUS_DISABLED'
    STATUS_DELETED = 'STATUS_DELETED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppUserStatus:
    r"""The satus of the applicaiton user."""
    details: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    r"""The details of applicaiton user status."""
    status: Optional[Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The application user status field."""
    

