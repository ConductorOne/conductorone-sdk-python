"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import updatepolicyrequest as shared_updatepolicyrequest, updatepolicyresponse as shared_updatepolicyresponse
from sdk.types import BaseModel
from sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIPolicyV1PoliciesUpdateRequestTypedDict(TypedDict):
    id: str
    update_policy_request: NotRequired[shared_updatepolicyrequest.UpdatePolicyRequestTypedDict]
    

class C1APIPolicyV1PoliciesUpdateRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    update_policy_request: Annotated[Optional[shared_updatepolicyrequest.UpdatePolicyRequest], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    

class C1APIPolicyV1PoliciesUpdateResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_policy_response: NotRequired[shared_updatepolicyresponse.UpdatePolicyResponseTypedDict]
    r"""The UpdatePolicyResponse message contains the updated policy object."""
    

class C1APIPolicyV1PoliciesUpdateResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_policy_response: Optional[shared_updatepolicyresponse.UpdatePolicyResponse] = None
    r"""The UpdatePolicyResponse message contains the updated policy object."""
    
