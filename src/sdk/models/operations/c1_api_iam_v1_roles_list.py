"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import listrolesresponse as shared_listrolesresponse
from typing import Optional


@dataclasses.dataclass
class C1APIIamV1RolesListRequest:
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIIamV1RolesListResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_roles_response: Optional[shared_listrolesresponse.ListRolesResponse] = dataclasses.field(default=None)
    r"""The ListRolesResponse message contains a list of results and a nextPageToken if applicable."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

