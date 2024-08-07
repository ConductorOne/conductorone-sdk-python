"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import getappusagecontrolsresponse as shared_getappusagecontrolsresponse
from sdk.types import BaseModel
from sdk.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1AppUsageControlsServiceGetRequestTypedDict(TypedDict):
    app_id: str
    

class C1APIAppV1AppUsageControlsServiceGetRequest(BaseModel):
    app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class C1APIAppV1AppUsageControlsServiceGetResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_app_usage_controls_response: NotRequired[shared_getappusagecontrolsresponse.GetAppUsageControlsResponseTypedDict]
    r"""The GetAppUsageControlsResponse message contains the retrieved AppUsageControls object."""
    

class C1APIAppV1AppUsageControlsServiceGetResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_app_usage_controls_response: Optional[shared_getappusagecontrolsresponse.GetAppUsageControlsResponse] = None
    r"""The GetAppUsageControlsResponse message contains the retrieved AppUsageControls object."""
    
