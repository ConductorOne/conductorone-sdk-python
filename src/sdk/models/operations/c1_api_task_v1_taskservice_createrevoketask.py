"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import taskservicecreaterevokeresponse as shared_taskservicecreaterevokeresponse
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class C1APITaskV1TaskServiceCreateRevokeTaskResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_service_create_revoke_response: NotRequired[shared_taskservicecreaterevokeresponse.TaskServiceCreateRevokeResponseTypedDict]
    r"""The TaskServiceCreateRevokeResponse returns a task view which has a task including JSONPATHs to the expanded items in the expanded array."""
    

class C1APITaskV1TaskServiceCreateRevokeTaskResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_service_create_revoke_response: Optional[shared_taskservicecreaterevokeresponse.TaskServiceCreateRevokeResponse] = None
    r"""The TaskServiceCreateRevokeResponse returns a task view which has a task including JSONPATHs to the expanded items in the expanded array."""
    
