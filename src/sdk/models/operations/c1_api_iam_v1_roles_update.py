"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import updaterolerequest as shared_updaterolerequest
from ...models.shared import updaterolesresponse as shared_updaterolesresponse
from typing import Optional


@dataclasses.dataclass
class C1APIIamV1RolesUpdateRequest:
    role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'role_id', 'style': 'simple', 'explode': False }})
    update_role_request: Optional[shared_updaterolerequest.UpdateRoleRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIIamV1RolesUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_roles_response: Optional[shared_updaterolesresponse.UpdateRolesResponse] = dataclasses.field(default=None)
    r"""UpdateRolesResponse is the response message containing the updated role."""
    

