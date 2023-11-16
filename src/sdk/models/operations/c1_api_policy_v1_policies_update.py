"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import updatepolicyrequest as shared_updatepolicyrequest
from ...models.shared import updatepolicyresponse as shared_updatepolicyresponse
from typing import Optional


@dataclasses.dataclass
class C1APIPolicyV1PoliciesUpdateRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    update_policy_request: Optional[shared_updatepolicyrequest.UpdatePolicyRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIPolicyV1PoliciesUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    update_policy_response: Optional[shared_updatepolicyresponse.UpdatePolicyResponse] = dataclasses.field(default=None)
    r"""The UpdatePolicyResponse message contains the updated policy object."""
    

