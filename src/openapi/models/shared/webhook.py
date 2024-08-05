"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class WebhookTypedDict(TypedDict):
    r"""The Webhook message."""
    
    created_at: NotRequired[datetime]
    deleted_at: NotRequired[datetime]
    description: NotRequired[str]
    r"""The description field."""
    display_name: NotRequired[str]
    r"""The displayName field."""
    id: NotRequired[str]
    r"""The id field."""
    updated_at: NotRequired[datetime]
    url: NotRequired[str]
    r"""The url field."""
    

class Webhook(BaseModel):
    r"""The Webhook message."""
    
    created_at: Annotated[Optional[datetime], pydantic.Field(alias="createdAt")] = None
    deleted_at: Annotated[Optional[datetime], pydantic.Field(alias="deletedAt")] = None
    description: Optional[str] = None
    r"""The description field."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The displayName field."""
    id: Optional[str] = None
    r"""The id field."""
    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
    url: Optional[str] = None
    r"""The url field."""
    
