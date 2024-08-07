"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import webhooksservicecreateresponse as shared_webhooksservicecreateresponse
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class C1APIWebhooksV1WebhooksServiceCreateResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhooks_service_create_response: NotRequired[shared_webhooksservicecreateresponse.WebhooksServiceCreateResponseTypedDict]
    r"""Successful response"""
    

class C1APIWebhooksV1WebhooksServiceCreateResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhooks_service_create_response: Optional[shared_webhooksservicecreateresponse.WebhooksServiceCreateResponse] = None
    r"""Successful response"""
    
