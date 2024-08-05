"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from openapi.types import BaseModel
import pydantic
from typing import Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppPopulationReportState(str, Enum):
    r"""The state field tracks the state of the AppPopulationReport. This state field can be one of REPORT_STATE_PENDING, REPORT_STATE_UNSPECIFIED, REPORT_STATE_OK, REPORT_STATE_ERROR."""
    REPORT_STATE_UNSPECIFIED = "REPORT_STATE_UNSPECIFIED"
    REPORT_STATE_PENDING = "REPORT_STATE_PENDING"
    REPORT_STATE_OK = "REPORT_STATE_OK"
    REPORT_STATE_ERROR = "REPORT_STATE_ERROR"

class AppPopulationReportTypedDict(TypedDict):
    r"""The AppPopulationReport is a generated report for a specific app that gives details about the app's users. These details include what groups, roles, and other entitlements the users have access to."""
    
    app_id: NotRequired[str]
    r"""The appId is the Id of the app which the report is generated for."""
    created_at: NotRequired[datetime]
    download_url: NotRequired[str]
    r"""The downloadUrl is the url used for downloading the AppPopulationReport."""
    hashes: NotRequired[Dict[str, str]]
    r"""The hashes field contains the file hashes of the report."""
    id: NotRequired[str]
    r"""The id field."""
    state: NotRequired[AppPopulationReportState]
    r"""The state field tracks the state of the AppPopulationReport. This state field can be one of REPORT_STATE_PENDING, REPORT_STATE_UNSPECIFIED, REPORT_STATE_OK, REPORT_STATE_ERROR."""
    

class AppPopulationReport(BaseModel):
    r"""The AppPopulationReport is a generated report for a specific app that gives details about the app's users. These details include what groups, roles, and other entitlements the users have access to."""
    
    app_id: Annotated[Optional[str], pydantic.Field(alias="appId")] = None
    r"""The appId is the Id of the app which the report is generated for."""
    created_at: Annotated[Optional[datetime], pydantic.Field(alias="createdAt")] = None
    download_url: Annotated[Optional[str], pydantic.Field(alias="downloadUrl")] = None
    r"""The downloadUrl is the url used for downloading the AppPopulationReport."""
    hashes: Optional[Dict[str, str]] = None
    r"""The hashes field contains the file hashes of the report."""
    id: Optional[str] = None
    r"""The id field."""
    state: Optional[AppPopulationReportState] = None
    r"""The state field tracks the state of the AppPopulationReport. This state field can be one of REPORT_STATE_PENDING, REPORT_STATE_UNSPECIFIED, REPORT_STATE_OK, REPORT_STATE_ERROR."""
    