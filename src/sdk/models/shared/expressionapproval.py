"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExpressionApproval:
    r"""The ExpressionApproval message."""
    allow_self_approval: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowSelfApproval'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow self approval of if the user is specified and also the target of the ticket."""
    assigned_user_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedUserIds') }})
    r"""The assignedUserIds field."""
    expressions: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expressions') }})
    r"""Array of dynamic expressions to determine the approvers.  The first expression to return a non-empty list of users will be used."""
    fallback: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallback'), 'exclude': lambda f: f is None }})
    r"""Configuration to allow a fallback if the expression does not return a valid list of users."""
    fallback_user_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallbackUserIds') }})
    r"""Configuration to specific which users to fallback to if and the expression does not return a valid list of users."""
    



@dataclasses.dataclass
class ExpressionApprovalInput:
    r"""The ExpressionApproval message."""
    

