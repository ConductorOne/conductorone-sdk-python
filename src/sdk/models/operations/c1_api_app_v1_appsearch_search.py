"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import searchappsresponse as shared_searchappsresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppSearchSearchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    search_apps_response: Optional[shared_searchappsresponse.SearchAppsResponse] = dataclasses.field(default=None)
    r"""The SearchAppsResponse message contains a list of results and a nextPageToken if applicable."""
    

