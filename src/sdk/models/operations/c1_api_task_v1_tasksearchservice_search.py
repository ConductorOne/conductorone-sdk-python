"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import tasksearchresponse as shared_tasksearchresponse
from typing import Optional


@dataclasses.dataclass
class C1APITaskV1TaskSearchServiceSearchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    task_search_response: Optional[shared_tasksearchresponse.TaskSearchResponse] = dataclasses.field(default=None)
    r"""The TaskSearchResponse message contains a list of results and a nextPageToken if applicable."""
    

