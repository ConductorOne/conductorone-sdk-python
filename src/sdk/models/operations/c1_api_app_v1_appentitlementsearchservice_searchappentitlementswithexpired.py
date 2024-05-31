"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import searchappentitlementswithexpiredresponse as shared_searchappentitlementswithexpiredresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppEntitlementSearchServiceSearchAppEntitlementsWithExpiredRequest:
    app_entitlement_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_entitlement_id', 'style': 'simple', 'explode': False }})
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIAppV1AppEntitlementSearchServiceSearchAppEntitlementsWithExpiredResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    search_app_entitlements_with_expired_response: Optional[shared_searchappentitlementswithexpiredresponse.SearchAppEntitlementsWithExpiredResponse] = dataclasses.field(default=None)
    r"""The SearchAppEntitlementsWithExpiredResponse message contains a list of results and a nextPageToken if applicable."""
    
