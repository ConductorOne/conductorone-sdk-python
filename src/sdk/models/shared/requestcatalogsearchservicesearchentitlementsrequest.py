"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appentitlementexpandmask as shared_appentitlementexpandmask
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class RequestCatalogSearchServiceSearchEntitlementsRequestGrantedStatus(str, Enum):
    r"""Search entitlements with this granted status for your signed in user."""
    UNSPECIFIED = 'UNSPECIFIED'
    ALL = 'ALL'
    GRANTED = 'GRANTED'
    NOT_GRANTED = 'NOT_GRANTED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RequestCatalogSearchServiceSearchEntitlementsRequest:
    r"""The RequestCatalogSearchServiceSearchEntitlementsRequest searches entitlements, but only ones that are available to you through the open catalogs."""
    app_display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appDisplayName'), 'exclude': lambda f: f is None }})
    r"""Search entitlements that belong to this app name (exact match)."""
    app_entitlement_expand_mask: Optional[shared_appentitlementexpandmask.AppEntitlementExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The app entitlement expand mask allows the user to get additional information when getting responses containing app entitlement views."""
    entitlement_alias: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entitlementAlias'), 'exclude': lambda f: f is None }})
    r"""Search for entitlements with this alias (exact match)."""
    granted_status: Optional[RequestCatalogSearchServiceSearchEntitlementsRequestGrantedStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantedStatus'), 'exclude': lambda f: f is None }})
    r"""Search entitlements with this granted status for your signed in user."""
    include_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('includeDeleted'), 'exclude': lambda f: f is None }})
    r"""Include deleted entitlements"""
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize'), 'exclude': lambda f: f is None }})
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageToken'), 'exclude': lambda f: f is None }})
    r"""The pageToken field."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    r"""Fuzzy search the display name of resource types."""
    

