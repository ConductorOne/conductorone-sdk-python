"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import appentitlementreference as shared_appentitlementreference
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ApprovedAction:
    r"""The approved action indicates that the approvalinstance had an outcome of approved."""
    approved_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approvedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    entitlements: Optional[List[shared_appentitlementreference.AppEntitlementReference]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entitlements') }})
    r"""The entitlements that were approved. This will only ever be a list of one entitlement."""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId'), 'exclude': lambda f: f is None }})
    r"""The UserID that approved this step."""
    

