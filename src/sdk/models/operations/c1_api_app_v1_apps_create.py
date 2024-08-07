"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import createappresponse as shared_createappresponse
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class C1APIAppV1AppsCreateResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    create_app_response: NotRequired[shared_createappresponse.CreateAppResponseTypedDict]
    r"""Returns the new app's values."""
    

class C1APIAppV1AppsCreateResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    create_app_response: Optional[shared_createappresponse.CreateAppResponse] = None
    r"""Returns the new app's values."""
    
