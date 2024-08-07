"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class WebhookRefTypedDict(TypedDict):
    r"""The WebhookRef message."""
    
    id: NotRequired[str]
    r"""The id field."""
    

class WebhookRef(BaseModel):
    r"""The WebhookRef message."""
    
    id: Optional[str] = None
    r"""The id field."""
    
