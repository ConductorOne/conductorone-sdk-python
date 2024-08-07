"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .app import App, AppTypedDict
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CreateAppResponseTypedDict(TypedDict):
    r"""Returns the new app's values."""
    
    app: NotRequired[AppTypedDict]
    r"""The App object provides all of the details for an app, as well as some configuration."""
    

class CreateAppResponse(BaseModel):
    r"""Returns the new app's values."""
    
    app: Optional[App] = None
    r"""The App object provides all of the details for an app, as well as some configuration."""
    
