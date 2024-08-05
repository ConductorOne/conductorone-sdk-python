"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import taskactionsservicerestartrequest as shared_taskactionsservicerestartrequest, taskactionsservicerestartresponse as shared_taskactionsservicerestartresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APITaskV1TaskActionsServiceRestartRequestTypedDict(TypedDict):
    task_id: str
    task_actions_service_restart_request: NotRequired[shared_taskactionsservicerestartrequest.TaskActionsServiceRestartRequestTypedDict]
    

class C1APITaskV1TaskActionsServiceRestartRequest(BaseModel):
    task_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    task_actions_service_restart_request: Annotated[Optional[shared_taskactionsservicerestartrequest.TaskActionsServiceRestartRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APITaskV1TaskActionsServiceRestartResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_actions_service_restart_response: NotRequired[shared_taskactionsservicerestartresponse.TaskActionsServiceRestartResponseTypedDict]
    r"""Successful response"""
    

class C1APITaskV1TaskActionsServiceRestartResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_actions_service_restart_response: Optional[shared_taskactionsservicerestartresponse.TaskActionsServiceRestartResponse] = None
    r"""Successful response"""
    