"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ConditionSucceededTypedDict(TypedDict):
    r"""The ConditionSucceeded message."""
    
    succeeded_at: NotRequired[datetime]
    

class ConditionSucceeded(BaseModel):
    r"""The ConditionSucceeded message."""
    
    succeeded_at: Annotated[Optional[datetime], pydantic.Field(alias="succeededAt")] = None
    