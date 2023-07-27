"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppEntitlementExpandMask:
    r"""The app entitlement expand mask allows the user to get additional information when getting responses containing app entitlement views."""
    paths: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paths'), 'exclude': lambda f: f is None }})
    r"""Array of strings to describe which items to expand on the return value. Can be any combination of \\"*\\", \\"app_id\\", \\"app_resource_type_id\\", or \\"app_resource_id\\"."""
    

