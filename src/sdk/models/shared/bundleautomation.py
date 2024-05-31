"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .bundleautomationlastrunstate import BundleAutomationLastRunState
from .bundleautomationruleentitlement import BundleAutomationRuleEntitlement
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BundleAutomation:
    r"""The BundleAutomation message.

    This message contains a oneof named conditions. Only a single field of the following list may be set at a time:
      - entitlements
    """
    UNSET='__SPEAKEASY_UNSET__'
    bundle_automation_last_run_state: Optional[BundleAutomationLastRunState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""The BundleAutomationLastRunState message."""
    bundle_automation_rule_entitlement: Optional[BundleAutomationRuleEntitlement] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entitlements'), 'exclude': lambda f: f is BundleAutomation.UNSET }})
    r"""The BundleAutomationRuleEntitlement message."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    request_catalog_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestCatalogId'), 'exclude': lambda f: f is None }})
    r"""The requestCatalogId field."""
    tenant_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tenantId'), 'exclude': lambda f: f is None }})
    r"""The tenantId field."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    
