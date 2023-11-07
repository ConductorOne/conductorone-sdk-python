"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import Optional

class Outcome(str, Enum):
    r"""The outcome of the certification."""
    CERTIFY_OUTCOME_UNSPECIFIED = 'CERTIFY_OUTCOME_UNSPECIFIED'
    CERTIFY_OUTCOME_CERTIFIED = 'CERTIFY_OUTCOME_CERTIFIED'
    CERTIFY_OUTCOME_DECERTIFIED = 'CERTIFY_OUTCOME_DECERTIFIED'
    CERTIFY_OUTCOME_ERROR = 'CERTIFY_OUTCOME_ERROR'
    CERTIFY_OUTCOME_CANCELLED = 'CERTIFY_OUTCOME_CANCELLED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskTypeCertify:
    r"""The TaskTypeCertify message indicates that a task is a certify task and all related details."""
    access_review_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessReviewId'), 'exclude': lambda f: f is None }})
    r"""The ID of the access review."""
    access_review_selection: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accessReviewSelection'), 'exclude': lambda f: f is None }})
    r"""The ID of the specific access review object that owns this certify task. This is also set on a revoke task if the revoke task is created from the denied outcome of a certify task."""
    app_entitlement_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app entitlement."""
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app."""
    app_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app user."""
    identity_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the user."""
    outcome: Optional[Outcome] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcome'), 'exclude': lambda f: f is None }})
    r"""The outcome of the certification."""
    outcome_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcomeTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class TaskTypeCertifyInput:
    r"""The TaskTypeCertify message indicates that a task is a certify task and all related details."""
    

