"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .taskexpandmask import TaskExpandMask, TaskExpandMaskTypedDict
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TaskServiceCreateRevokeRequestTypedDict(TypedDict):
    r"""Create a revoke task."""
    
    app_entitlement_id: str
    r"""The ID of the app entitlement to revoke access to."""
    app_id: str
    r"""The ID of the app associated with the entitlement."""
    task_expand_mask: NotRequired[TaskExpandMaskTypedDict]
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    app_user_id: NotRequired[str]
    r"""The ID of the app user to revoke access from. This field and identityUserId cannot both be set for a given request."""
    description: NotRequired[str]
    r"""The description of the request."""
    identity_user_id: NotRequired[str]
    r"""The ID of the user associated with the app user we are revoking access from. This field cannot be set if appUserID is also set."""
    

class TaskServiceCreateRevokeRequest(BaseModel):
    r"""Create a revoke task."""
    
    app_entitlement_id: Annotated[str, pydantic.Field(alias="appEntitlementId")]
    r"""The ID of the app entitlement to revoke access to."""
    app_id: Annotated[str, pydantic.Field(alias="appId")]
    r"""The ID of the app associated with the entitlement."""
    task_expand_mask: Annotated[Optional[TaskExpandMask], pydantic.Field(alias="expandMask")] = None
    r"""The task expand mask is an array of strings that specifes the related objects the requester wishes to have returned when making a request where the expand mask is part of the input. Use '*' to view all possible responses."""
    app_user_id: Annotated[Optional[str], pydantic.Field(alias="appUserId")] = None
    r"""The ID of the app user to revoke access from. This field and identityUserId cannot both be set for a given request."""
    description: Optional[str] = None
    r"""The description of the request."""
    identity_user_id: Annotated[Optional[str], pydantic.Field(alias="identityUserId")] = None
    r"""The ID of the user associated with the app user we are revoking access from. This field cannot be set if appUserID is also set."""
    
