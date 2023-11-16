"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connectorservicegetresponse as shared_connectorservicegetresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAppV1ConnectorServiceGetRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class C1APIAppV1ConnectorServiceGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    connector_service_get_response: Optional[shared_connectorservicegetresponse.ConnectorServiceGetResponse] = dataclasses.field(default=None)
    r"""The ConnectorServiceGetResponse message contains the connectorView, and an expand mask."""
    

