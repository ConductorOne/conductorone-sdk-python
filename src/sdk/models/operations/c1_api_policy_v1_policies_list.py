"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listpolicyresponse as shared_listpolicyresponse
from typing import Optional



@dataclasses.dataclass
class C1APIPolicyV1PoliciesListRequest:
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class C1APIPolicyV1PoliciesListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_policy_response: Optional[shared_listpolicyresponse.ListPolicyResponse] = dataclasses.field(default=None)
    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

