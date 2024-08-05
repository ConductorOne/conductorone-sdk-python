"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .taskexpandmask import TaskExpandMask, TaskExpandMaskTypedDict
from .taskref import TaskRef, TaskRefTypedDict
from .tasktype_input import TaskTypeInput, TaskTypeInputTypedDict
from datetime import datetime
from enum import Enum
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AccountTypes(str, Enum):
    APP_USER_TYPE_UNSPECIFIED = "APP_USER_TYPE_UNSPECIFIED"
    APP_USER_TYPE_USER = "APP_USER_TYPE_USER"
    APP_USER_TYPE_SERVICE_ACCOUNT = "APP_USER_TYPE_SERVICE_ACCOUNT"
    APP_USER_TYPE_SYSTEM_ACCOUNT = "APP_USER_TYPE_SYSTEM_ACCOUNT"

class CurrentStep(str, Enum):
    r"""Search tasks that have this type of step as the current step."""
    TASK_SEARCH_CURRENT_STEP_UNSPECIFIED = "TASK_SEARCH_CURRENT_STEP_UNSPECIFIED"
    TASK_SEARCH_CURRENT_STEP_APPROVAL = "TASK_SEARCH_CURRENT_STEP_APPROVAL"
    TASK_SEARCH_CURRENT_STEP_PROVISION = "TASK_SEARCH_CURRENT_STEP_PROVISION"

class EmergencyStatus(str, Enum):
    r"""Search tasks that are or are not emergency access."""
    UNSPECIFIED = "UNSPECIFIED"
    ALL = "ALL"
    NON_EMERGENCY = "NON_EMERGENCY"
    EMERGENCY = "EMERGENCY"

class SortBy(str, Enum):
    r"""Sort tasks in a specific order."""
    TASK_SEARCH_SORT_BY_UNSPECIFIED = "TASK_SEARCH_SORT_BY_UNSPECIFIED"
    TASK_SEARCH_SORT_BY_ACCOUNT = "TASK_SEARCH_SORT_BY_ACCOUNT"
    TASK_SEARCH_SORT_BY_RESOURCE = "TASK_SEARCH_SORT_BY_RESOURCE"
    TASK_SEARCH_SORT_BY_ACCOUNT_OWNER = "TASK_SEARCH_SORT_BY_ACCOUNT_OWNER"
    TASK_SEARCH_SORT_BY_REVERSE_TICKET_ID = "TASK_SEARCH_SORT_BY_REVERSE_TICKET_ID"

class TaskStates(str, Enum):
    TASK_STATE_UNSPECIFIED = "TASK_STATE_UNSPECIFIED"
    TASK_STATE_OPEN = "TASK_STATE_OPEN"
    TASK_STATE_CLOSED = "TASK_STATE_CLOSED"

class TaskSearchRequestTypedDict(TypedDict):
    r"""Search for tasks based on a plethora filters."""
    
    task_expand_mask: NotRequired[TaskExpandMaskTypedDict]
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    access_review_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that belong to any of the access reviews included in this list."""
    account_owner_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that have any of these account owners."""
    account_types: NotRequired[Nullable[List[AccountTypes]]]
    r"""The accountTypes field."""
    actor_id: NotRequired[str]
    r"""Search tasks that have this actor ID."""
    app_entitlement_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that have any of these app entitlement IDs."""
    app_resource_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that have any of these app resource IDs."""
    app_resource_type_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that have any of these app resource type IDs."""
    app_user_subject_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that have any of these app users as subjects."""
    application_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that have any of these apps as targets."""
    assignees_in_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks by  List of UserIDs which are currently assigned these Tasks"""
    created_after: NotRequired[datetime]
    created_before: NotRequired[datetime]
    current_step: NotRequired[CurrentStep]
    r"""Search tasks that have this type of step as the current step."""
    emergency_status: NotRequired[EmergencyStatus]
    r"""Search tasks that are or are not emergency access."""
    exclude_app_entitlement_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that do not have any of these app entitlement IDs."""
    exclude_ids: NotRequired[Nullable[List[str]]]
    r"""Exclude Specific TaskIDs from this serach result."""
    include_deleted: NotRequired[bool]
    r"""Whether or not to include deleted tasks."""
    my_work_user_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks where the user would see this task in the My Work section"""
    older_than_duration: NotRequired[str]
    opener_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that were created by any of the users in this array."""
    page_size: NotRequired[int]
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: NotRequired[str]
    r"""The pageToken field."""
    previously_acted_on_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks that were acted on by any of these users."""
    query: NotRequired[str]
    r"""Fuzzy search tasks by display name or description. Also can search by numeric ID."""
    refs: NotRequired[Nullable[List[TaskRefTypedDict]]]
    r"""Query tasks by display name, description, or numeric ID."""
    sort_by: NotRequired[SortBy]
    r"""Sort tasks in a specific order."""
    subject_ids: NotRequired[Nullable[List[str]]]
    r"""Search tasks where these users are the subject."""
    task_states: NotRequired[Nullable[List[TaskStates]]]
    r"""Search tasks with this task state."""
    task_types: NotRequired[Nullable[List[TaskTypeInputTypedDict]]]
    r"""Search tasks with this task type. This is a oneOf, and needs an object, which can be empty, to sort."""
    

class TaskSearchRequest(BaseModel):
    r"""Search for tasks based on a plethora filters."""
    
    task_expand_mask: Annotated[Optional[TaskExpandMask], pydantic.Field(alias="expandMask")] = None
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    access_review_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="accessReviewIds")] = UNSET
    r"""Search tasks that belong to any of the access reviews included in this list."""
    account_owner_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="accountOwnerIds")] = UNSET
    r"""Search tasks that have any of these account owners."""
    account_types: Annotated[OptionalNullable[List[AccountTypes]], pydantic.Field(alias="accountTypes")] = UNSET
    r"""The accountTypes field."""
    actor_id: Annotated[Optional[str], pydantic.Field(alias="actorId")] = None
    r"""Search tasks that have this actor ID."""
    app_entitlement_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="appEntitlementIds")] = UNSET
    r"""Search tasks that have any of these app entitlement IDs."""
    app_resource_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="appResourceIds")] = UNSET
    r"""Search tasks that have any of these app resource IDs."""
    app_resource_type_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="appResourceTypeIds")] = UNSET
    r"""Search tasks that have any of these app resource type IDs."""
    app_user_subject_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="appUserSubjectIds")] = UNSET
    r"""Search tasks that have any of these app users as subjects."""
    application_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="applicationIds")] = UNSET
    r"""Search tasks that have any of these apps as targets."""
    assignees_in_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="assigneesInIds")] = UNSET
    r"""Search tasks by  List of UserIDs which are currently assigned these Tasks"""
    created_after: Annotated[Optional[datetime], pydantic.Field(alias="createdAfter")] = None
    created_before: Annotated[Optional[datetime], pydantic.Field(alias="createdBefore")] = None
    current_step: Annotated[Optional[CurrentStep], pydantic.Field(alias="currentStep")] = None
    r"""Search tasks that have this type of step as the current step."""
    emergency_status: Annotated[Optional[EmergencyStatus], pydantic.Field(alias="emergencyStatus")] = None
    r"""Search tasks that are or are not emergency access."""
    exclude_app_entitlement_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="excludeAppEntitlementIds")] = UNSET
    r"""Search tasks that do not have any of these app entitlement IDs."""
    exclude_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="excludeIds")] = UNSET
    r"""Exclude Specific TaskIDs from this serach result."""
    include_deleted: Annotated[Optional[bool], pydantic.Field(alias="includeDeleted")] = None
    r"""Whether or not to include deleted tasks."""
    my_work_user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="myWorkUserIds")] = UNSET
    r"""Search tasks where the user would see this task in the My Work section"""
    older_than_duration: Annotated[Optional[str], pydantic.Field(alias="olderThanDuration")] = None
    opener_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="openerIds")] = UNSET
    r"""Search tasks that were created by any of the users in this array."""
    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Annotated[Optional[str], pydantic.Field(alias="pageToken")] = None
    r"""The pageToken field."""
    previously_acted_on_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="previouslyActedOnIds")] = UNSET
    r"""Search tasks that were acted on by any of these users."""
    query: Optional[str] = None
    r"""Fuzzy search tasks by display name or description. Also can search by numeric ID."""
    refs: OptionalNullable[List[TaskRef]] = UNSET
    r"""Query tasks by display name, description, or numeric ID."""
    sort_by: Annotated[Optional[SortBy], pydantic.Field(alias="sortBy")] = None
    r"""Sort tasks in a specific order."""
    subject_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="subjectIds")] = UNSET
    r"""Search tasks where these users are the subject."""
    task_states: Annotated[OptionalNullable[List[TaskStates]], pydantic.Field(alias="taskStates")] = UNSET
    r"""Search tasks with this task state."""
    task_types: Annotated[OptionalNullable[List[TaskTypeInput]], pydantic.Field(alias="taskTypes")] = UNSET
    r"""Search tasks with this task type. This is a oneOf, and needs an object, which can be empty, to sort."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["TaskExpandMask", "accessReviewIds", "accountOwnerIds", "accountTypes", "actorId", "appEntitlementIds", "appResourceIds", "appResourceTypeIds", "appUserSubjectIds", "applicationIds", "assigneesInIds", "createdAfter", "createdBefore", "currentStep", "emergencyStatus", "excludeAppEntitlementIds", "excludeIds", "includeDeleted", "myWorkUserIds", "olderThanDuration", "openerIds", "pageSize", "pageToken", "previouslyActedOnIds", "query", "refs", "sortBy", "subjectIds", "taskStates", "taskTypes"]
        nullable_fields = ["accessReviewIds", "accountOwnerIds", "accountTypes", "appEntitlementIds", "appResourceIds", "appResourceTypeIds", "appUserSubjectIds", "applicationIds", "assigneesInIds", "excludeAppEntitlementIds", "excludeIds", "myWorkUserIds", "openerIds", "previouslyActedOnIds", "refs", "subjectIds", "taskStates", "taskTypes"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        
