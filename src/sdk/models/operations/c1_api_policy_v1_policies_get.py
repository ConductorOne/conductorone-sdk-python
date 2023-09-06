"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getpolicyresponse as shared_getpolicyresponse
from typing import Optional



@dataclasses.dataclass
class C1APIPolicyV1PoliciesGetRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class C1APIPolicyV1PoliciesGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_policy_response: Optional[shared_getpolicyresponse.GetPolicyResponse] = dataclasses.field(default=None)
    r"""The GetPolicyResponse message contains the policy object."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

