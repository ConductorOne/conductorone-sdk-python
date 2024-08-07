"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import getpolicyresponse as shared_getpolicyresponse
from sdk.types import BaseModel
from sdk.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIPolicyV1PoliciesGetRequestTypedDict(TypedDict):
    id: str
    

class C1APIPolicyV1PoliciesGetRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class C1APIPolicyV1PoliciesGetResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_policy_response: NotRequired[shared_getpolicyresponse.GetPolicyResponseTypedDict]
    r"""The GetPolicyResponse message contains the policy object."""
    

class C1APIPolicyV1PoliciesGetResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_policy_response: Optional[shared_getpolicyresponse.GetPolicyResponse] = None
    r"""The GetPolicyResponse message contains the policy object."""
    
