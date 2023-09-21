"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accept as shared_accept
from ..shared import approval as shared_approval
from ..shared import provision as shared_provision
from ..shared import reject as shared_reject
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PolicyStep:
    r"""The PolicyStep message.

    This message contains a oneof named step. Only a single field of the following list may be set at a time:
      - approval
      - provision
      - accept
      - reject
    """
    accept: Optional[shared_accept.Accept] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accept'), 'exclude': lambda f: f is None }})
    r"""This policy step indicates that a ticket should have an approved outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    approval: Optional[shared_approval.Approval] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approval'), 'exclude': lambda f: f is None }})
    r"""The Approval message.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
      - users
      - manager
      - appOwners
      - group
      - self
      - entitlementOwners
      - expression
    """
    provision: Optional[shared_provision.Provision] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provision'), 'exclude': lambda f: f is None }})
    r"""The provision step references a provision policy for this step."""
    reject: Optional[shared_reject.Reject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reject'), 'exclude': lambda f: f is None }})
    r"""This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PolicyStepInput:
    r"""The PolicyStep message.

    This message contains a oneof named step. Only a single field of the following list may be set at a time:
      - approval
      - provision
      - accept
      - reject
    """
    accept: Optional[shared_accept.Accept] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accept'), 'exclude': lambda f: f is None }})
    r"""This policy step indicates that a ticket should have an approved outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    approval: Optional[shared_approval.ApprovalInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approval'), 'exclude': lambda f: f is None }})
    r"""The Approval message.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
      - users
      - manager
      - appOwners
      - group
      - self
      - entitlementOwners
      - expression
    """
    provision: Optional[shared_provision.Provision] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provision'), 'exclude': lambda f: f is None }})
    r"""The provision step references a provision policy for this step."""
    reject: Optional[shared_reject.Reject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reject'), 'exclude': lambda f: f is None }})
    r"""This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    

