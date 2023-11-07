"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .taskgrantsource import TaskGrantSource
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import Optional

class TaskTypeGrantOutcome(str, Enum):
    r"""The outcome of the grant."""
    GRANT_OUTCOME_UNSPECIFIED = 'GRANT_OUTCOME_UNSPECIFIED'
    GRANT_OUTCOME_GRANTED = 'GRANT_OUTCOME_GRANTED'
    GRANT_OUTCOME_DENIED = 'GRANT_OUTCOME_DENIED'
    GRANT_OUTCOME_ERROR = 'GRANT_OUTCOME_ERROR'
    GRANT_OUTCOME_CANCELLED = 'GRANT_OUTCOME_CANCELLED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskTypeGrant:
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    app_entitlement_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app entitlement."""
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app."""
    app_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app user."""
    grant_duration: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantDuration'), 'exclude': lambda f: f is None }})
    identity_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the user."""
    outcome: Optional[TaskTypeGrantOutcome] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcome'), 'exclude': lambda f: f is None }})
    r"""The outcome of the grant."""
    outcome_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcomeTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    task_grant_source: Optional[TaskGrantSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaskTypeGrantInput:
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    task_grant_source: Optional[TaskGrantSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket."""
    

