"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import updateapprequest as shared_updateapprequest
from ...models.shared import updateappresponse as shared_updateappresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1AppsUpdateRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    update_app_request: Optional[shared_updateapprequest.UpdateAppRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAppV1AppsUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_app_response: Optional[shared_updateappresponse.UpdateAppResponse] = dataclasses.field(default=None)
    r"""Returns the updated app's new values."""
    

