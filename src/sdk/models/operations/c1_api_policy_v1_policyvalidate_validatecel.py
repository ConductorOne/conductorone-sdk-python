"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import validatepolicycelresponse as shared_validatepolicycelresponse
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class C1APIPolicyV1PolicyValidateValidateCELResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    validate_policy_cel_response: NotRequired[shared_validatepolicycelresponse.ValidatePolicyCELResponseTypedDict]
    r"""Successful response"""
    

class C1APIPolicyV1PolicyValidateValidateCELResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    validate_policy_cel_response: Optional[shared_validatepolicycelresponse.ValidatePolicyCELResponse] = None
    r"""Successful response"""
    
