"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BundleAutomationLastRunStateStatus(str, Enum):
    r"""The status field."""
    BUNDLE_AUTOMATION_RUN_STATUS_UNSPECIFIED = "BUNDLE_AUTOMATION_RUN_STATUS_UNSPECIFIED"
    BUNDLE_AUTOMATION_RUN_STATUS_SUCCESS = "BUNDLE_AUTOMATION_RUN_STATUS_SUCCESS"
    BUNDLE_AUTOMATION_RUN_STATUS_FAILURE = "BUNDLE_AUTOMATION_RUN_STATUS_FAILURE"
    BUNDLE_AUTOMATION_RUN_STATUS_IN_PROGRESS = "BUNDLE_AUTOMATION_RUN_STATUS_IN_PROGRESS"

class BundleAutomationLastRunStateTypedDict(TypedDict):
    r"""The BundleAutomationLastRunState message."""
    
    last_run_at: NotRequired[datetime]
    status: NotRequired[BundleAutomationLastRunStateStatus]
    r"""The status field."""
    

class BundleAutomationLastRunState(BaseModel):
    r"""The BundleAutomationLastRunState message."""
    
    last_run_at: Annotated[Optional[datetime], pydantic.Field(alias="lastRunAt")] = None
    status: Optional[BundleAutomationLastRunStateStatus] = None
    r"""The status field."""
    
