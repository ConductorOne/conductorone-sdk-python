"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import appaccessrequestdefaults as shared_appaccessrequestdefaults, cancelaccessrequestdefaultsrequest as shared_cancelaccessrequestdefaultsrequest
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1AppAccessRequestsDefaultsServiceCancelAppAccessRequestsDefaultsRequestTypedDict(TypedDict):
    app_id: str
    cancel_access_request_defaults_request: NotRequired[shared_cancelaccessrequestdefaultsrequest.CancelAccessRequestDefaultsRequestTypedDict]
    

class C1APIAppV1AppAccessRequestsDefaultsServiceCancelAppAccessRequestsDefaultsRequest(BaseModel):
    app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    cancel_access_request_defaults_request: Annotated[Optional[shared_cancelaccessrequestdefaultsrequest.CancelAccessRequestDefaultsRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APIAppV1AppAccessRequestsDefaultsServiceCancelAppAccessRequestsDefaultsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    app_access_request_defaults: NotRequired[shared_appaccessrequestdefaults.AppAccessRequestDefaultsTypedDict]
    r"""Successful response"""
    

class C1APIAppV1AppAccessRequestsDefaultsServiceCancelAppAccessRequestsDefaultsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    app_access_request_defaults: Optional[shared_appaccessrequestdefaults.AppAccessRequestDefaults] = None
    r"""Successful response"""
    
