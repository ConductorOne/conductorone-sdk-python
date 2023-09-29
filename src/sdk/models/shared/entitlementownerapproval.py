"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EntitlementOwnerApproval:
    r"""The entitlement owner approval allows configuration of the approval step when the target approvers are the entitlement owners."""
    allow_self_approval: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowSelfApproval'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow self approval if the target user is an entitlement owner during this step."""
    fallback: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallback'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow a fallback if the entitlement owner cannot be identified."""
    fallback_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallbackUserIds') }})
    r"""Configuration to specific which users to fallback to if fallback is enabled and the entitlement owner cannot be identified."""
    




@dataclasses.dataclass
class EntitlementOwnerApprovalInput:
    r"""The entitlement owner approval allows configuration of the approval step when the target approvers are the entitlement owners."""
    

