"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import requestcatalogmanagementservicelistentitlementsforaccessresponse as shared_requestcatalogmanagementservicelistentitlementsforaccessresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessRequestTypedDict(TypedDict):
    catalog_id: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessRequest(BaseModel):
    catalog_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    page_size: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    page_token: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_list_entitlements_for_access_response: NotRequired[shared_requestcatalogmanagementservicelistentitlementsforaccessresponse.RequestCatalogManagementServiceListEntitlementsForAccessResponseTypedDict]
    r"""The RequestCatalogManagementServiceListEntitlementsForAccessResponse message contains a list of results and a nextPageToken if applicable."""
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_management_service_list_entitlements_for_access_response: Optional[shared_requestcatalogmanagementservicelistentitlementsforaccessresponse.RequestCatalogManagementServiceListEntitlementsForAccessResponse] = None
    r"""The RequestCatalogManagementServiceListEntitlementsForAccessResponse message contains a list of results and a nextPageToken if applicable."""
    