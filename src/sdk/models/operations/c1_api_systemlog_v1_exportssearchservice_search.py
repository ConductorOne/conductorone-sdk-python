"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import exportssearchservicesearchresponse as shared_exportssearchservicesearchresponse
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class C1APISystemlogV1ExportsSearchServiceSearchResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    exports_search_service_search_response: NotRequired[shared_exportssearchservicesearchresponse.ExportsSearchServiceSearchResponseTypedDict]
    r"""Successful response"""
    

class C1APISystemlogV1ExportsSearchServiceSearchResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    exports_search_service_search_response: Optional[shared_exportssearchservicesearchresponse.ExportsSearchServiceSearchResponse] = None
    r"""Successful response"""
    
