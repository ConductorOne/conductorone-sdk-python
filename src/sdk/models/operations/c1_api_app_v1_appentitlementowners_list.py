"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listappentitlementownersresponse as shared_listappentitlementownersresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppEntitlementOwnersListRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    entitlement_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entitlement_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIAppV1AppEntitlementOwnersListResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_app_entitlement_owners_response: Optional[shared_listappentitlementownersresponse.ListAppEntitlementOwnersResponse] = dataclasses.field(default=None)
    r"""The response message for listing app entitlement owners."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

