"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import listappentitlementownersresponse as shared_listappentitlementownersresponse
from sdk.types import BaseModel
from sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1AppEntitlementOwnersListRequestTypedDict(TypedDict):
    app_id: str
    entitlement_id: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    

class C1APIAppV1AppEntitlementOwnersListRequest(BaseModel):
    app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    entitlement_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    page_size: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    page_token: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class C1APIAppV1AppEntitlementOwnersListResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_app_entitlement_owners_response: NotRequired[shared_listappentitlementownersresponse.ListAppEntitlementOwnersResponseTypedDict]
    r"""The response message for listing app entitlement owners."""
    

class C1APIAppV1AppEntitlementOwnersListResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_app_entitlement_owners_response: Optional[shared_listappentitlementownersresponse.ListAppEntitlementOwnersResponse] = None
    r"""The response message for listing app entitlement owners."""
    
