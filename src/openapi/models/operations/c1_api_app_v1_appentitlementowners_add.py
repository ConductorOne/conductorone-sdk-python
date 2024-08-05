"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import addappentitlementownerrequest as shared_addappentitlementownerrequest, addappentitlementownerresponse as shared_addappentitlementownerresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1AppEntitlementOwnersAddRequestTypedDict(TypedDict):
    app_id: str
    entitlement_id: str
    add_app_entitlement_owner_request: NotRequired[shared_addappentitlementownerrequest.AddAppEntitlementOwnerRequestTypedDict]
    

class C1APIAppV1AppEntitlementOwnersAddRequest(BaseModel):
    app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    entitlement_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    add_app_entitlement_owner_request: Annotated[Optional[shared_addappentitlementownerrequest.AddAppEntitlementOwnerRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APIAppV1AppEntitlementOwnersAddResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    add_app_entitlement_owner_response: NotRequired[shared_addappentitlementownerresponse.AddAppEntitlementOwnerResponseTypedDict]
    r"""The empty response message for adding an app entitlement owner."""
    

class C1APIAppV1AppEntitlementOwnersAddResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    add_app_entitlement_owner_response: Optional[shared_addappentitlementownerresponse.AddAppEntitlementOwnerResponse] = None
    r"""The empty response message for adding an app entitlement owner."""
    
