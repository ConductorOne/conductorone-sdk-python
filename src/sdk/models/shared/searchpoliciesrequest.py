"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import policyref as shared_policyref
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class SearchPoliciesRequestPolicyTypes(str, Enum):
    POLICY_TYPE_UNSPECIFIED = 'POLICY_TYPE_UNSPECIFIED'
    POLICY_TYPE_GRANT = 'POLICY_TYPE_GRANT'
    POLICY_TYPE_REVOKE = 'POLICY_TYPE_REVOKE'
    POLICY_TYPE_CERTIFY = 'POLICY_TYPE_CERTIFY'
    POLICY_TYPE_ACCESS_REQUEST = 'POLICY_TYPE_ACCESS_REQUEST'
    POLICY_TYPE_PROVISION = 'POLICY_TYPE_PROVISION'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchPoliciesRequest:
    r"""Search Policies by a few properties."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""Search for policies with a case insensitive match on the display name."""
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize'), 'exclude': lambda f: f is None }})
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageToken'), 'exclude': lambda f: f is None }})
    r"""The pageToken field."""
    policy_types: Optional[list[SearchPoliciesRequestPolicyTypes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyTypes') }})
    r"""The policy type to search on. This can be POLICY_TYPE_GRANT, POLICY_TYPE_REVOKE, POLICY_TYPE_CERTIFY, POLICY_TYPE_ACCESS_REQUEST, or POLICY_TYPE_PROVISION."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    r"""Query the policies with a fuzzy search on display name and description."""
    refs: Optional[list[shared_policyref.PolicyRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refs') }})
    r"""The refs field."""
    

