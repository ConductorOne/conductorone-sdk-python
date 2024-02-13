"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connectorexpandmask import ConnectorExpandMask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorServiceCreateDelegatedRequest:
    r"""The ConnectorServiceCreateDelegatedRequest message contains the fields required to create a connector."""
    UNSET='__SPEAKEASY_UNSET__'
    connector_expand_mask: Optional[ConnectorExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The ConnectorExpandMask is used to expand related objects on a connector."""
    catalog_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalogId'), 'exclude': lambda f: f is None }})
    r"""The catalogId describes which catalog entry this connector is an instance of. For example, every Okta connector will have the same catalogId indicating it is an Okta connector."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the connector."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The displayName of the connector."""
    user_ids: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIds'), 'exclude': lambda f: f is ConnectorServiceCreateDelegatedRequest.UNSET }})
    r"""The userIds field is used to define the integration owners of the connector."""
    

