"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import createpolicyresponse as shared_createpolicyresponse
from typing import Optional


@dataclasses.dataclass
class C1APIPolicyV1PoliciesCreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_policy_response: Optional[shared_createpolicyresponse.CreatePolicyResponse] = dataclasses.field(default=None)
    r"""The CreatePolicyResponse message contains the created policy object."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

