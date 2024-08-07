"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import updateapprequest as shared_updateapprequest, updateappresponse as shared_updateappresponse
from sdk.types import BaseModel
from sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1AppsUpdateRequestTypedDict(TypedDict):
    id: str
    update_app_request: NotRequired[shared_updateapprequest.UpdateAppRequestTypedDict]
    

class C1APIAppV1AppsUpdateRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    update_app_request: Annotated[Optional[shared_updateapprequest.UpdateAppRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APIAppV1AppsUpdateResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_app_response: NotRequired[shared_updateappresponse.UpdateAppResponseTypedDict]
    r"""Returns the updated app's new values."""
    

class C1APIAppV1AppsUpdateResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_app_response: Optional[shared_updateappresponse.UpdateAppResponse] = None
    r"""Returns the updated app's new values."""
    
