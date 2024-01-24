"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .appentitlementexpandmask import AppEntitlementExpandMask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppEntitlementSearchServiceSearchRequest:
    r"""Search app entitlements by a variety of filters."""
    access_review_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessReviewId'), 'exclude': lambda f: f is None }})
    r"""Search for app entitlements that are being reviewed as part of this access review campaign."""
    alias: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alias'), 'exclude': lambda f: f is None }})
    r"""Search for app entitlements that have this alias (exact match)."""
    app_entitlement_expand_mask: Optional[AppEntitlementExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The app entitlement expand mask allows the user to get additional information when getting responses containing app entitlement views."""
    app_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appIds') }})
    r"""Search for app entitlements contained in any of these apps."""
    app_user_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserIds') }})
    r"""Search for app entitlements that are granted to any of these app user ids."""
    compliance_framework_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('complianceFrameworkIds') }})
    r"""Search for app entitlements that are part of these compliace frameworks."""
    exclude_app_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeAppIds') }})
    r"""Exclude app entitlements from the results that are in these app IDs."""
    exclude_app_user_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('excludeAppUserIds') }})
    r"""Exclude app entitlements from the results that these app users have granted."""
    include_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('includeDeleted'), 'exclude': lambda f: f is None }})
    r"""Include deleted app entitlements, this includes app entitlements that have a deleted parent object (app, app resource, app resource type)"""
    only_get_expiring: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onlyGetExpiring'), 'exclude': lambda f: f is None }})
    r"""Restrict results to only those who have expiring app entitlement user bindings."""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageSize'), 'exclude': lambda f: f is None }})
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pageToken'), 'exclude': lambda f: f is None }})
    r"""The pageToken field."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    r"""Query the app entitlements with a fuzzy search on display name and description."""
    resource_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceIds') }})
    r"""Search for app entitlements that belongs to these resources."""
    resource_type_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceTypeIds') }})
    r"""Search for app entitlements that are for items with resources types that have matching names. Example names are \\"group\\", \\"role\\", and \\"app\\"."""
    risk_level_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('riskLevelIds') }})
    r"""Search for app entitlements with these risk levels."""
    

