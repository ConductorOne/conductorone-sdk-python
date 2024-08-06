"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import systemlogservicelisteventsresponse as shared_systemlogservicelisteventsresponse
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class C1APISystemlogV1SystemLogServiceListEventsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    system_log_service_list_events_response: NotRequired[shared_systemlogservicelisteventsresponse.SystemLogServiceListEventsResponseTypedDict]
    r"""Successful response"""
    

class C1APISystemlogV1SystemLogServiceListEventsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    system_log_service_list_events_response: Optional[shared_systemlogservicelisteventsresponse.SystemLogServiceListEventsResponse] = None
    r"""Successful response"""
    