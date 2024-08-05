"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import listrolesresponse as shared_listrolesresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIIamV1RolesListRequestTypedDict(TypedDict):
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    

class C1APIIamV1RolesListRequest(BaseModel):
    page_size: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    page_token: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    

class C1APIIamV1RolesListResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_roles_response: NotRequired[shared_listrolesresponse.ListRolesResponseTypedDict]
    r"""The ListRolesResponse message contains a list of results and a nextPageToken if applicable."""
    

class C1APIIamV1RolesListResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_roles_response: Optional[shared_listrolesresponse.ListRolesResponse] = None
    r"""The ListRolesResponse message contains a list of results and a nextPageToken if applicable."""
    