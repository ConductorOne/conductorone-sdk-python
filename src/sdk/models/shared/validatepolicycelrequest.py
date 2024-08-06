"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ValidatePolicyCELRequestTypedDict(TypedDict):
    r"""The ValidatePolicyCELRequest message."""
    
    cel: NotRequired[str]
    r"""The cel field."""
    

class ValidatePolicyCELRequest(BaseModel):
    r"""The ValidatePolicyCELRequest message."""
    
    cel: Optional[str] = None
    r"""The cel field."""
    