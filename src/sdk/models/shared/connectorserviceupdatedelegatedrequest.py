"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import connector as shared_connector
from ..shared import connectorexpandmask as shared_connectorexpandmask
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorServiceUpdateDelegatedRequestInput:
    r"""The ConnectorServiceUpdateDelegatedRequest message contains the fields required to update a connector."""
    connector: Optional[shared_connector.ConnectorInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connector'), 'exclude': lambda f: f is None }})
    r"""A Connector is used to sync objects into Apps"""
    connector_expand_mask: Optional[shared_connectorexpandmask.ConnectorExpandMask] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandMask'), 'exclude': lambda f: f is None }})
    r"""The ConnectorExpandMask is used to expand related objects on a connector."""
    update_mask: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateMask') }})
    

