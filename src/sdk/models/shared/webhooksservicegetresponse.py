"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhook import Webhook, WebhookTypedDict
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class WebhooksServiceGetResponseTypedDict(TypedDict):
    r"""The WebhooksServiceGetResponse message."""
    
    webhook: NotRequired[WebhookTypedDict]
    r"""The Webhook message."""
    

class WebhooksServiceGetResponse(BaseModel):
    r"""The WebhooksServiceGetResponse message."""
    
    webhook: Optional[Webhook] = None
    r"""The Webhook message."""
    