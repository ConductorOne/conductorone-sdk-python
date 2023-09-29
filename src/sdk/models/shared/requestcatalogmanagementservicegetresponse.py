"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import requestcatalogview as shared_requestcatalogview
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RequestCatalogManagementServiceGetResponse:
    r"""The request catalog management service get response returns a request catalog view with the expanded items in the expanded array indicated by the expand mask in the request."""
    expanded: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expanded') }})
    r"""List of serialized related objects."""
    request_catalog_view: Optional[shared_requestcatalogview.RequestCatalogView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestCatalogView'), 'exclude': lambda f: f is None }})
    r"""The request catalog view contains the serialized request catalog and paths to objects referenced by the request catalog."""
    

