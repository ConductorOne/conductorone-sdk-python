"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import taskactionsservicedenyrequest as shared_taskactionsservicedenyrequest, taskactionsservicedenyresponse as shared_taskactionsservicedenyresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APITaskV1TaskActionsServiceDenyRequestTypedDict(TypedDict):
    task_id: str
    task_actions_service_deny_request: NotRequired[shared_taskactionsservicedenyrequest.TaskActionsServiceDenyRequestTypedDict]
    

class C1APITaskV1TaskActionsServiceDenyRequest(BaseModel):
    task_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    task_actions_service_deny_request: Annotated[Optional[shared_taskactionsservicedenyrequest.TaskActionsServiceDenyRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APITaskV1TaskActionsServiceDenyResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_actions_service_deny_response: NotRequired[shared_taskactionsservicedenyresponse.TaskActionsServiceDenyResponseTypedDict]
    r"""The TaskActionsServiceDenyResponse returns a task view with paths indicating the location of expanded items in the array."""
    

class C1APITaskV1TaskActionsServiceDenyResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_actions_service_deny_response: Optional[shared_taskactionsservicedenyresponse.TaskActionsServiceDenyResponse] = None
    r"""The TaskActionsServiceDenyResponse returns a task view with paths indicating the location of expanded items in the array."""
    