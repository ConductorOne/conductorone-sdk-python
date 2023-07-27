"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appentitlementview as shared_appentitlementview
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateAppEntitlementResponse:
    r"""The UpdateAppEntitlementResponse message."""
    app_entitlement_view: Optional[shared_appentitlementview.AppEntitlementView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementView'), 'exclude': lambda f: f is None }})
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    expanded: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expanded'), 'exclude': lambda f: f is None }})
    r"""List of related objects"""
    

