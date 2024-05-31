"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .provisionpolicy import ProvisionPolicy
from .provisiontarget import ProvisionTarget
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Provision:
    r"""The provision step references a provision policy for this step."""
    provision_policy: Optional[ProvisionPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provisionPolicy'), 'exclude': lambda f: f is None }})
    r"""ProvisionPolicy is a oneOf that indicates how a provision step should be processed.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
      - connector
      - manual
      - delegated
      - webhook
      - multiStep
    """
    provision_target: Optional[ProvisionTarget] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provisionTarget'), 'exclude': lambda f: f is None }})
    r"""ProvisionTarget indicates the specific app, app entitlement, and if known, the app user and grant duration of this provision step"""
    assigned: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assigned'), 'exclude': lambda f: f is None }})
    r"""A field indicating whether this step is assigned."""
    

