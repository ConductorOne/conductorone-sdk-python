"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TaskRevokeSourceNonUsageTypedDict(TypedDict):
    r"""The TaskRevokeSourceNonUsage message indicates that the source of the revoke task is due to the grant not being used."""
    
    expires_at: NotRequired[datetime]
    last_login: NotRequired[datetime]
    

class TaskRevokeSourceNonUsage(BaseModel):
    r"""The TaskRevokeSourceNonUsage message indicates that the source of the revoke task is due to the grant not being used."""
    
    expires_at: Annotated[Optional[datetime], pydantic.Field(alias="expiresAt")] = None
    last_login: Annotated[Optional[datetime], pydantic.Field(alias="lastLogin")] = None
    