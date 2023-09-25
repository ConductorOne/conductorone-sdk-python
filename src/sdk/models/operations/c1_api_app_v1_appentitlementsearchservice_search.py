"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import appentitlementsearchservicesearchresponse as shared_appentitlementsearchservicesearchresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppEntitlementSearchServiceSearchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    app_entitlement_search_service_search_response: Optional[shared_appentitlementsearchservicesearchresponse.AppEntitlementSearchServiceSearchResponse] = dataclasses.field(default=None)
    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

