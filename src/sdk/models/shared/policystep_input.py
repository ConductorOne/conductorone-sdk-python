"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accept import Accept
from .approval_input import ApprovalInput
from .provision import Provision
from .reject import Reject
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


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
    accept: Optional[Accept] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accept') }})
    r"""This policy step indicates that a ticket should have an approved outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    approval: Optional[ApprovalInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approval') }})
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
    provision: Optional[Provision] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provision') }})
    r"""The provision step references a provision policy for this step."""
    reject: Optional[Reject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reject') }})
    r"""This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps."""
    

