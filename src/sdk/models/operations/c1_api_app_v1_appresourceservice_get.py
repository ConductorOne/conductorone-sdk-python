"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import appresourceservicegetresponse as shared_appresourceservicegetresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppResourceServiceGetRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    app_resource_type_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_resource_type_id', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class C1APIAppV1AppResourceServiceGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    app_resource_service_get_response: Optional[shared_appresourceservicegetresponse.AppResourceServiceGetResponse] = dataclasses.field(default=None)
    r"""The app resource service get response contains the app resource view and array of expanded items indicated by the request's expand mask."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

