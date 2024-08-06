"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ResponsePolicyApprovalStepDenyTypedDict(TypedDict):
    r"""The ResponsePolicyApprovalStepDeny message."""
    
    comment: NotRequired[str]
    r"""optional comment"""
    

class ResponsePolicyApprovalStepDeny(BaseModel):
    r"""The ResponsePolicyApprovalStepDeny message."""
    
    comment: Optional[str] = None
    r"""optional comment"""
    