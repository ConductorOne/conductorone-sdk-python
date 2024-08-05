"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .policy import Policy, PolicyTypedDict
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CreatePolicyResponseTypedDict(TypedDict):
    r"""The CreatePolicyResponse message contains the created policy object."""
    
    policy: NotRequired[PolicyTypedDict]
    r"""A policy describes the behavior of the ConductorOne system when processing a task. You can describe the type, approvers, fallback behavior, and escalation processes."""
    

class CreatePolicyResponse(BaseModel):
    r"""The CreatePolicyResponse message contains the created policy object."""
    
    policy: Optional[Policy] = None
    r"""A policy describes the behavior of the ConductorOne system when processing a task. You can describe the type, approvers, fallback behavior, and escalation processes."""
    
