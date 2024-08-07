"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class WebhookSourceApprovalStepTypedDict(TypedDict):
    r"""The WebhookSourceApprovalStep message."""
    
    ticket_id: NotRequired[str]
    r"""The ticketId field."""
    

class WebhookSourceApprovalStep(BaseModel):
    r"""The WebhookSourceApprovalStep message."""
    
    ticket_id: Annotated[Optional[str], pydantic.Field(alias="ticketId")] = None
    r"""The ticketId field."""
    
