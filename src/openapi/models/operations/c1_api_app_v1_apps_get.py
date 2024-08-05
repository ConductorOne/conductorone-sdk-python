"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import getappresponse as shared_getappresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1AppsGetRequestTypedDict(TypedDict):
    id: str
    

class C1APIAppV1AppsGetRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class C1APIAppV1AppsGetResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_app_response: NotRequired[shared_getappresponse.GetAppResponseTypedDict]
    r"""The GetAppResponse message contains the details of the requested app in the app field."""
    

class C1APIAppV1AppsGetResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_app_response: Optional[shared_getappresponse.GetAppResponse] = None
    r"""The GetAppResponse message contains the details of the requested app in the app field."""
    
