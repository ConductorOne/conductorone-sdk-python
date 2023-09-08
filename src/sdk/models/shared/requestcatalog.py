"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import appentitlement as shared_appentitlement
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RequestCatalog:
    r"""The RequestCatalog is used for managing which entitlements are requestable, and who can request them."""
    access_entitlements: Optional[list[shared_appentitlement.AppEntitlement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessEntitlements'), 'exclude': lambda f: f is None }})
    r"""An array of app entitlements that, if the user has, can view the contents of this catalog."""
    app_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appIds'), 'exclude': lambda f: f is None }})
    r"""The Apps contained in this request catalog."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    created_by_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdByUserId'), 'exclude': lambda f: f is None }})
    r"""The id of the user this request catalog was created by."""
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the request catalog."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the request catalog."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The id of the request catalog."""
    published: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('published'), 'exclude': lambda f: f is None }})
    r"""Whether or not this catalog is published."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    visible_to_everyone: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visibleToEveryone'), 'exclude': lambda f: f is None }})
    r"""If this is true, the access entitlement requirement is ignored."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RequestCatalogInput:
    r"""The RequestCatalog is used for managing which entitlements are requestable, and who can request them."""
    access_entitlements: Optional[list[shared_appentitlement.AppEntitlementInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessEntitlements'), 'exclude': lambda f: f is None }})
    r"""An array of app entitlements that, if the user has, can view the contents of this catalog."""
    app_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appIds'), 'exclude': lambda f: f is None }})
    r"""The Apps contained in this request catalog."""
    created_by_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdByUserId'), 'exclude': lambda f: f is None }})
    r"""The id of the user this request catalog was created by."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the request catalog."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the request catalog."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The id of the request catalog."""
    published: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('published'), 'exclude': lambda f: f is None }})
    r"""Whether or not this catalog is published."""
    visible_to_everyone: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visibleToEveryone'), 'exclude': lambda f: f is None }})
    r"""If this is true, the access entitlement requirement is ignored."""
    

