"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listappsresponse as shared_listappsresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppsListRequest:
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class C1APIAppV1AppsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_apps_response: Optional[shared_listappsresponse.ListAppsResponse] = dataclasses.field(default=None)
    r"""The ListAppsResponse message contains a list of results and a nextPageToken if applicable."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

