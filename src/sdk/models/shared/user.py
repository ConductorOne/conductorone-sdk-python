"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import userattributemappingsource as shared_userattributemappingsource
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from sdk import utils
from typing import Any, Optional, Union

class UserDirectoryStatus(str, Enum):
    r"""The status of the user in the directory."""
    UNKNOWN = 'UNKNOWN'
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'
    DELETED = 'DELETED'



@dataclasses.dataclass
class UserProfile3:
    pass



@dataclasses.dataclass
class UserProfile:
    pass

class UserStatus(str, Enum):
    r"""The status of the user in the system."""
    UNKNOWN = 'UNKNOWN'
    ENABLED = 'ENABLED'
    DISABLED = 'DISABLED'
    DELETED = 'DELETED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class User:
    r"""The User object provides all of the details for an user, as well as some configuration."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    delegated_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delegatedUserId'), 'exclude': lambda f: f is None }})
    r"""The id of the user to whom tasks will be automatically reassigned to."""
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    department: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('department'), 'exclude': lambda f: f is None }})
    r"""The department which the user belongs to in the organization."""
    department_sources: Optional[list[shared_userattributemappingsource.UserAttributeMappingSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('departmentSources') }})
    r"""A list of objects mapped based on department attribute mappings configured in the system."""
    directory_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('directoryIds') }})
    r"""A list of unique ids that represent different directories."""
    directory_status: Optional[UserDirectoryStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('directoryStatus'), 'exclude': lambda f: f is None }})
    r"""The status of the user in the directory."""
    directory_status_sources: Optional[list[shared_userattributemappingsource.UserAttributeMappingSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('directoryStatusSources') }})
    r"""A list of objects mapped based on directoryStatus attribute mappings configured in the system."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the user."""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""This is the user's email."""
    emails: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emails') }})
    r"""This is a list of all of the user's emails from app users."""
    employment_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employmentStatus'), 'exclude': lambda f: f is None }})
    r"""The users employment status."""
    employment_status_sources: Optional[list[shared_userattributemappingsource.UserAttributeMappingSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employmentStatusSources') }})
    r"""A list of objects mapped based on employmentStatus attribute mappings configured in the system."""
    employment_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employmentType'), 'exclude': lambda f: f is None }})
    r"""The employment type of the user."""
    employment_type_sources: Optional[list[shared_userattributemappingsource.UserAttributeMappingSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employmentTypeSources') }})
    r"""A list of objects mapped based on employmentType attribute mappings configured in the system."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""A unique identifier of the user."""
    job_title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobTitle'), 'exclude': lambda f: f is None }})
    r"""The job title of the user."""
    job_title_sources: Optional[list[shared_userattributemappingsource.UserAttributeMappingSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobTitleSources') }})
    r"""A list of objects mapped based on jobTitle attribute mappings configured in the system."""
    manager_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('managerIds') }})
    r"""A list of ids of the user's managers."""
    manager_sources: Optional[list[shared_userattributemappingsource.UserAttributeMappingSource]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('managerSources') }})
    r"""A list of objects mapped based on managerId attribute mappings configured in the system."""
    profile: Optional[dict[str, Union[str, float, UserProfile3, list[Any], bool]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('profile'), 'exclude': lambda f: f is None }})
    role_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('roleIds') }})
    r"""A list of unique identifiers that maps to ConductorOne’s user roles let you assign users permissions tailored to the work they do in the software."""
    status: Optional[UserStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the user in the system."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    r"""This is the user's primary username. Typically sourced from the primary directory."""
    usernames: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('usernames') }})
    r"""This is a list of all of the user's usernames from app users."""
    

