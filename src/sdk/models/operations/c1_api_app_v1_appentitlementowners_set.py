"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import setappentitlementownersrequest as shared_setappentitlementownersrequest
from ..shared import setappentitlementownersresponse as shared_setappentitlementownersresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppEntitlementOwnersSetRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    entitlement_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entitlement_id', 'style': 'simple', 'explode': False }})
    set_app_entitlement_owners_request: Optional[shared_setappentitlementownersrequest.SetAppEntitlementOwnersRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class C1APIAppV1AppEntitlementOwnersSetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    set_app_entitlement_owners_response: Optional[shared_setappentitlementownersresponse.SetAppEntitlementOwnersResponse] = dataclasses.field(default=None)
    r"""The empty response message for setting the app entitlement owners."""
    
