"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connectorcredential import ConnectorCredential
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectorServiceRotateCredentialResponse:
    r"""ConnectorServiceRotateCredentialResponse is the response returned by the rotate method."""
    connector_credential: Optional[ConnectorCredential] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credential'), 'exclude': lambda f: f is None }})
    r"""ConnectorCredential is used by a connector to authenticate with conductor one."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientSecret'), 'exclude': lambda f: f is None }})
    r"""The new clientSecret returned after rotating the connector credential."""
    

