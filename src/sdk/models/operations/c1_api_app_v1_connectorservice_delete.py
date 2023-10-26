"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectorservicedeleterequest as shared_connectorservicedeleterequest
from ..shared import connectorservicedeleteresponse as shared_connectorservicedeleteresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1ConnectorServiceDeleteRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    connector_service_delete_request: Optional[shared_connectorservicedeleterequest.ConnectorServiceDeleteRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAppV1ConnectorServiceDeleteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connector_service_delete_response: Optional[shared_connectorservicedeleteresponse.ConnectorServiceDeleteResponse] = dataclasses.field(default=None)
    r"""Empty response body. Status code indicates success."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

