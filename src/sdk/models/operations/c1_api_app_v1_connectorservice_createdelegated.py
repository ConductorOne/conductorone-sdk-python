"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connectorservicecreatedelegatedrequest as shared_connectorservicecreatedelegatedrequest
from ...models.shared import connectorservicecreateresponse as shared_connectorservicecreateresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1ConnectorServiceCreateDelegatedRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    connector_service_create_delegated_request: Optional[shared_connectorservicecreatedelegatedrequest.ConnectorServiceCreateDelegatedRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIAppV1ConnectorServiceCreateDelegatedResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connector_service_create_response: Optional[shared_connectorservicecreateresponse.ConnectorServiceCreateResponse] = dataclasses.field(default=None)
    r"""The ConnectorServiceCreateResponse is the response returned from creating a connector."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

