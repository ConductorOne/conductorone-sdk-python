"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import requestcatalogmanagementservicelistresponse as shared_requestcatalogmanagementservicelistresponse
from typing import Optional


@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceListRequest:
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceListResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_list_response: Optional[shared_requestcatalogmanagementservicelistresponse.RequestCatalogManagementServiceListResponse] = dataclasses.field(default=None)
    r"""Successful response"""
    

