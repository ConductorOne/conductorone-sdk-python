"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import requestcatalogmanagementserviceaddaccessentitlementsrequest as shared_requestcatalogmanagementserviceaddaccessentitlementsrequest
from ..shared import requestcatalogmanagementserviceaddaccessentitlementsresponse as shared_requestcatalogmanagementserviceaddaccessentitlementsresponse
from typing import Optional



@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsRequest:
    catalog_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'catalog_id', 'style': 'simple', 'explode': False }})
    request_catalog_management_service_add_access_entitlements_request: Optional[shared_requestcatalogmanagementserviceaddaccessentitlementsrequest.RequestCatalogManagementServiceAddAccessEntitlementsRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_add_access_entitlements_response: Optional[shared_requestcatalogmanagementserviceaddaccessentitlementsresponse.RequestCatalogManagementServiceAddAccessEntitlementsResponse] = dataclasses.field(default=None)
    r"""Empty response with a status code indicating success."""
    

