"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import requestcatalogmanagementserviceaddappentitlementsrequest as shared_requestcatalogmanagementserviceaddappentitlementsrequest
from ...models.shared import requestcatalogmanagementserviceaddappentitlementsresponse as shared_requestcatalogmanagementserviceaddappentitlementsresponse
from typing import Optional


@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalog_id', 'style': 'simple', 'explode': False }})
    request_catalog_management_service_add_app_entitlements_request: Optional[shared_requestcatalogmanagementserviceaddappentitlementsrequest.RequestCatalogManagementServiceAddAppEntitlementsRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    request_catalog_management_service_add_app_entitlements_response: Optional[shared_requestcatalogmanagementserviceaddappentitlementsresponse.RequestCatalogManagementServiceAddAppEntitlementsResponse] = dataclasses.field(default=None)
    r"""Empty response with a status code indicating success."""
    

