"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import taskservicegetresponse as shared_taskservicegetresponse
from typing import Optional



@dataclasses.dataclass
class C1APITaskV1TaskServiceGetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class C1APITaskV1TaskServiceGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_service_get_response: Optional[shared_taskservicegetresponse.TaskServiceGetResponse] = dataclasses.field(default=None)
    r"""The TaskServiceGetResponse returns a task view which has a task including JSONPATHs to the expanded items in the expanded array."""
    

