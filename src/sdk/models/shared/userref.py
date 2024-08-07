"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UserRefTypedDict(TypedDict):
    r"""A reference to a user."""
    
    id: NotRequired[str]
    r"""The id of the user."""
    

class UserRef(BaseModel):
    r"""A reference to a user."""
    
    id: Optional[str] = None
    r"""The id of the user."""
    
