"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import taskrevokesource as shared_taskrevokesource
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskTypeRevokeInput:
    r"""The TaskTypeRevoke message indicates that a task is a revoke task and all related details."""
    task_revoke_source: Optional[shared_taskrevokesource.TaskRevokeSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The TaskRevokeSource message indicates the source of the revoke task is one of expired, nonUsage, request, or review.

    This message contains a oneof named origin. Only a single field of the following list may be set at a time:
      - review
      - request
      - expired
      - nonUsage
    """
    


class TaskTypeRevokeOutcome(str, Enum):
    r"""The outcome of the revoke."""
    REVOKE_OUTCOME_UNSPECIFIED = 'REVOKE_OUTCOME_UNSPECIFIED'
    REVOKE_OUTCOME_REVOKED = 'REVOKE_OUTCOME_REVOKED'
    REVOKE_OUTCOME_DENIED = 'REVOKE_OUTCOME_DENIED'
    REVOKE_OUTCOME_ERROR = 'REVOKE_OUTCOME_ERROR'
    REVOKE_OUTCOME_CANCELLED = 'REVOKE_OUTCOME_CANCELLED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskTypeRevoke:
    r"""The TaskTypeRevoke message indicates that a task is a revoke task and all related details."""
    app_entitlement_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appEntitlementId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app entitlement."""
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app."""
    app_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app user."""
    identity_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identityUserId'), 'exclude': lambda f: f is None }})
    r"""The ID of the user."""
    outcome: Optional[TaskTypeRevokeOutcome] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcome'), 'exclude': lambda f: f is None }})
    r"""The outcome of the revoke."""
    outcome_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outcomeTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    task_revoke_source: Optional[shared_taskrevokesource.TaskRevokeSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The TaskRevokeSource message indicates the source of the revoke task is one of expired, nonUsage, request, or review.

    This message contains a oneof named origin. Only a single field of the following list may be set at a time:
      - review
      - request
      - expired
      - nonUsage
    """
    

