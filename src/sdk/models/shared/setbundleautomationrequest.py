"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .bundleautomationruleentitlement import BundleAutomationRuleEntitlement
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SetBundleAutomationRequest:
    r"""The SetBundleAutomationRequest message.

    This message contains a oneof named conditions. Only a single field of the following list may be set at a time:
      - entitlements
    """
    UNSET='__SPEAKEASY_UNSET__'
    bundle_automation_rule_entitlement: Optional[BundleAutomationRuleEntitlement] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entitlements'), 'exclude': lambda f: f is SetBundleAutomationRequest.UNSET }})
    r"""The BundleAutomationRuleEntitlement message."""
    

