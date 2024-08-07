"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import connectorserviceupdatedelegatedrequest as shared_connectorserviceupdatedelegatedrequest, connectorserviceupdateresponse as shared_connectorserviceupdateresponse
from sdk.types import BaseModel
from sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1ConnectorServiceUpdateDelegatedRequestTypedDict(TypedDict):
    connector_app_id: str
    connector_id: str
    connector_service_update_delegated_request: NotRequired[shared_connectorserviceupdatedelegatedrequest.ConnectorServiceUpdateDelegatedRequestTypedDict]
    

class C1APIAppV1ConnectorServiceUpdateDelegatedRequest(BaseModel):
    connector_app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    connector_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    connector_service_update_delegated_request: Annotated[Optional[shared_connectorserviceupdatedelegatedrequest.ConnectorServiceUpdateDelegatedRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APIAppV1ConnectorServiceUpdateDelegatedResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    connector_service_update_response: NotRequired[shared_connectorserviceupdateresponse.ConnectorServiceUpdateResponseTypedDict]
    r"""ConnectorServiceUpdateResponse is the response returned by the update method."""
    

class C1APIAppV1ConnectorServiceUpdateDelegatedResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    connector_service_update_response: Optional[shared_connectorserviceupdateresponse.ConnectorServiceUpdateResponse] = None
    r"""ConnectorServiceUpdateResponse is the response returned by the update method."""
    
