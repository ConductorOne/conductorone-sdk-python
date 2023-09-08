"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import appuserview as shared_appuserview
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppEntitlementUserView:
    r"""The AppEntitlementUserView (aka grant view) describes the relationship between an app user and an entitlement. They have more recently been referred to as grants."""
    app_entitlement_user_binding_created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementUserBindingCreatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    app_entitlement_user_binding_deprovision_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementUserBindingDeprovisionAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    app_user_view: Optional[shared_appuserview.AppUserView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUser'), 'exclude': lambda f: f is None }})
    r"""The AppUserView contains an app user as well as paths for apps, identity users, and last usage in expanded arrays."""
    

