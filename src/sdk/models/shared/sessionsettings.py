"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SessionSettingsTypedDict(TypedDict):
    r"""The SessionSettings message."""
    
    max_session_length: NotRequired[str]
    

class SessionSettings(BaseModel):
    r"""The SessionSettings message."""
    
    max_session_length: Annotated[Optional[str], pydantic.Field(alias="maxSessionLength")] = None
    
