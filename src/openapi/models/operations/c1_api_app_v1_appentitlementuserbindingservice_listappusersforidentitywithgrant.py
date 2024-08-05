"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import listappusersforidentitywithgrantresponse as shared_listappusersforidentitywithgrantresponse
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantRequestTypedDict(TypedDict):
    app_entitlement_id: str
    app_id: str
    identity_user_id: str
    

class C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantRequest(BaseModel):
    app_entitlement_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    identity_user_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_app_users_for_identity_with_grant_response: NotRequired[shared_listappusersforidentitywithgrantresponse.ListAppUsersForIdentityWithGrantResponseTypedDict]
    r"""Successful response"""
    

class C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    list_app_users_for_identity_with_grant_response: Optional[shared_listappusersforidentitywithgrantresponse.ListAppUsersForIdentityWithGrantResponse] = None
    r"""Successful response"""
    