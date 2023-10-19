"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appentitlementref as shared_appentitlementref
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RequestCatalogManagementServiceRemoveAppEntitlementsRequest:
    r"""The RequestCatalogManagementServiceRemoveAppEntitlementsRequest message is used to remove app entitlements from a request catalog."""
    app_entitlements: Optional[List[shared_appentitlementref.AppEntitlementRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlements') }})
    r"""The list of app entitlements to remove from the catalog."""
    

