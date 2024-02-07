"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import requestcatalogmanagementservicedeleterequest as shared_requestcatalogmanagementservicedeleterequest
from ...models.shared import requestcatalogmanagementservicedeleteresponse as shared_requestcatalogmanagementservicedeleteresponse
from typing import Optional


@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    request_catalog_management_service_delete_request: Optional[shared_requestcatalogmanagementservicedeleterequest.RequestCatalogManagementServiceDeleteRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_delete_response: Optional[shared_requestcatalogmanagementservicedeleteresponse.RequestCatalogManagementServiceDeleteResponse] = dataclasses.field(default=None)
    r"""Empty response with a status code indicating success."""
    

