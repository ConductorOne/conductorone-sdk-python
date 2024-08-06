"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RejectInstanceTypedDict(TypedDict):
    r"""This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps.
    The instance is just a marker for it being copied into an active policy.
    """
    
    reject_message: NotRequired[str]
    r"""An optional message to include in the comments when a task is automatically rejected."""
    

class RejectInstance(BaseModel):
    r"""This policy step indicates that a ticket should have a denied outcome. This is a terminal approval state and is used to explicitly define the end of approval steps.
    The instance is just a marker for it being copied into an active policy.
    """
    
    reject_message: Annotated[Optional[str], pydantic.Field(alias="rejectMessage")] = None
    r"""An optional message to include in the comments when a task is automatically rejected."""
    