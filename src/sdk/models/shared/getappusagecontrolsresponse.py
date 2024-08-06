"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appusagecontrols import AppUsageControls, AppUsageControlsTypedDict
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetAppUsageControlsResponseTypedDict(TypedDict):
    r"""The GetAppUsageControlsResponse message contains the retrieved AppUsageControls object."""
    
    app_usage_controls: NotRequired[AppUsageControlsTypedDict]
    r"""The AppUsageControls object describes some peripheral configuration for an app."""
    has_usage_data: NotRequired[bool]
    r"""HasUsageData is false if the access entitlement for this app has no usage data."""
    

class GetAppUsageControlsResponse(BaseModel):
    r"""The GetAppUsageControlsResponse message contains the retrieved AppUsageControls object."""
    
    app_usage_controls: Annotated[Optional[AppUsageControls], pydantic.Field(alias="appUsageControls")] = None
    r"""The AppUsageControls object describes some peripheral configuration for an app."""
    has_usage_data: Annotated[Optional[bool], pydantic.Field(alias="hasUsageData")] = None
    r"""HasUsageData is false if the access entitlement for this app has no usage data."""
    