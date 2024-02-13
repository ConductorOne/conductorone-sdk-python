"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connector import ConnectorInput
from .connectorexpandmask import ConnectorExpandMask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorServiceUpdateRequest:
    r"""The ConnectorServiceUpdateRequest message contains the fields required to update a connector."""
    UNSET='__SPEAKEASY_UNSET__'
    connector: Optional[ConnectorInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connector'), 'exclude': lambda f: f is None }})
    r"""A Connector is used to sync objects into Apps"""
    connector_expand_mask: Optional[ConnectorExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The ConnectorExpandMask is used to expand related objects on a connector."""
    update_mask: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateMask'), 'exclude': lambda f: f is ConnectorServiceUpdateRequest.UNSET }})
    

