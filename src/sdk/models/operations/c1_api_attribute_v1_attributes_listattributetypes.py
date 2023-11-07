"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import listattributetypesresponse as shared_listattributetypesresponse
from typing import Optional


@dataclasses.dataclass
class C1APIAttributeV1AttributesListAttributeTypesRequest:
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class C1APIAttributeV1AttributesListAttributeTypesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_attribute_types_response: Optional[shared_listattributetypesresponse.ListAttributeTypesResponse] = dataclasses.field(default=None)
    r"""ListAttributeTypesResponse is the response for listing attribute types."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

