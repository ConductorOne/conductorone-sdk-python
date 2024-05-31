"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import webhooksservicedeleterequest as shared_webhooksservicedeleterequest
from ...models.shared import webhooksservicedeleteresponse as shared_webhooksservicedeleteresponse
from typing import Optional


@dataclasses.dataclass
class C1APIWebhooksV1WebhooksServiceDeleteRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    webhooks_service_delete_request: Optional[shared_webhooksservicedeleterequest.WebhooksServiceDeleteRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class C1APIWebhooksV1WebhooksServiceDeleteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    webhooks_service_delete_response: Optional[shared_webhooksservicedeleteresponse.WebhooksServiceDeleteResponse] = dataclasses.field(default=None)
    r"""Empty response body. Status code indicates success."""
    
