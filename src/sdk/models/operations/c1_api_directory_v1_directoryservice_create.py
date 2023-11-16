"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import directoryservicecreateresponse as shared_directoryservicecreateresponse
from typing import Optional


@dataclasses.dataclass
class C1APIDirectoryV1DirectoryServiceCreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    directory_service_create_response: Optional[shared_directoryservicecreateresponse.DirectoryServiceCreateResponse] = dataclasses.field(default=None)
    r"""The DirectoryServiceCreateResponse message."""
    

