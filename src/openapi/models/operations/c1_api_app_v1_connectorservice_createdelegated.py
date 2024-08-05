"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import connectorservicecreatedelegatedrequest as shared_connectorservicecreatedelegatedrequest, connectorservicecreateresponse as shared_connectorservicecreateresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1ConnectorServiceCreateDelegatedRequestTypedDict(TypedDict):
    app_id: str
    connector_service_create_delegated_request: NotRequired[shared_connectorservicecreatedelegatedrequest.ConnectorServiceCreateDelegatedRequestTypedDict]
    

class C1APIAppV1ConnectorServiceCreateDelegatedRequest(BaseModel):
    app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    connector_service_create_delegated_request: Annotated[Optional[shared_connectorservicecreatedelegatedrequest.ConnectorServiceCreateDelegatedRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APIAppV1ConnectorServiceCreateDelegatedResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    connector_service_create_response: NotRequired[shared_connectorservicecreateresponse.ConnectorServiceCreateResponseTypedDict]
    r"""The ConnectorServiceCreateResponse is the response returned from creating a connector."""
    

class C1APIAppV1ConnectorServiceCreateDelegatedResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    connector_service_create_response: Optional[shared_connectorservicecreateresponse.ConnectorServiceCreateResponse] = None
    r"""The ConnectorServiceCreateResponse is the response returned from creating a connector."""
    
