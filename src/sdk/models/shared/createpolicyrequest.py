"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import policypostactions as shared_policypostactions
from ..shared import policysteps as shared_policysteps
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Dict, List, Optional

class CreatePolicyRequestPolicyType(str, Enum):
    r"""The enum of the policy type."""
    POLICY_TYPE_UNSPECIFIED = 'POLICY_TYPE_UNSPECIFIED'
    POLICY_TYPE_GRANT = 'POLICY_TYPE_GRANT'
    POLICY_TYPE_REVOKE = 'POLICY_TYPE_REVOKE'
    POLICY_TYPE_CERTIFY = 'POLICY_TYPE_CERTIFY'
    POLICY_TYPE_ACCESS_REQUEST = 'POLICY_TYPE_ACCESS_REQUEST'
    POLICY_TYPE_PROVISION = 'POLICY_TYPE_PROVISION'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreatePolicyRequestInput:
    r"""The CreatePolicyRequest message is used to create a new policy."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the new policy."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the new policy."""
    policy_steps: Optional[Dict[str, shared_policysteps.PolicyStepsInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policySteps'), 'exclude': lambda f: f is None }})
    r"""The map of policy type to policy steps. The key is the stringified version of the enum. See other policies for examples."""
    policy_type: Optional[CreatePolicyRequestPolicyType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyType'), 'exclude': lambda f: f is None }})
    r"""The enum of the policy type."""
    post_actions: Optional[List[shared_policypostactions.PolicyPostActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postActions') }})
    r"""Actions to occur after a policy finishes. As of now this is only valid on a certify policy to remediate a denied certification immediately."""
    reassign_tasks_to_delegates: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reassignTasksToDelegates'), 'exclude': lambda f: f is None }})
    r"""Allows reassigning tasks to delegates."""
    

