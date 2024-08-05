"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import requestcatalogmanagementserviceremoveaccessentitlementsrequest as shared_requestcatalogmanagementserviceremoveaccessentitlementsrequest, requestcatalogmanagementserviceremoveaccessentitlementsresponse as shared_requestcatalogmanagementserviceremoveaccessentitlementsresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsRequestTypedDict(TypedDict):
    catalog_id: str
    request_catalog_management_service_remove_access_entitlements_request: NotRequired[shared_requestcatalogmanagementserviceremoveaccessentitlementsrequest.RequestCatalogManagementServiceRemoveAccessEntitlementsRequestTypedDict]
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsRequest(BaseModel):
    catalog_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    request_catalog_management_service_remove_access_entitlements_request: Annotated[Optional[shared_requestcatalogmanagementserviceremoveaccessentitlementsrequest.RequestCatalogManagementServiceRemoveAccessEntitlementsRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_remove_access_entitlements_response: NotRequired[shared_requestcatalogmanagementserviceremoveaccessentitlementsresponse.RequestCatalogManagementServiceRemoveAccessEntitlementsResponseTypedDict]
    r"""Empty response with a status code indicating success."""
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_remove_access_entitlements_response: Optional[shared_requestcatalogmanagementserviceremoveaccessentitlementsresponse.RequestCatalogManagementServiceRemoveAccessEntitlementsResponse] = None
    r"""Empty response with a status code indicating success."""
    