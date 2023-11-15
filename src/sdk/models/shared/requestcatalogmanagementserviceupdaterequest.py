"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .requestcatalog_input import RequestCatalogInput
from .requestcatalogexpandmask import RequestCatalogExpandMask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RequestCatalogManagementServiceUpdateRequest:
    r"""Update a request catalog object by ID."""
    request_catalog: Optional[RequestCatalogInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog'), 'exclude': lambda f: f is None }})
    r"""The RequestCatalog is used for managing which entitlements are requestable, and who can request them."""
    request_catalog_expand_mask: Optional[RequestCatalogExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The RequestCatalogExpandMask includes the paths in the catalog view to expand in the return value of this call."""
    update_mask: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateMask') }})
    

