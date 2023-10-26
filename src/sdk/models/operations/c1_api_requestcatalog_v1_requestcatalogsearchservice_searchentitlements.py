"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import requestcatalogsearchservicesearchentitlementsresponse as shared_requestcatalogsearchservicesearchentitlementsresponse
from typing import Optional


@dataclasses.dataclass
class C1APIRequestcatalogV1RequestCatalogSearchServiceSearchEntitlementsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    request_catalog_search_service_search_entitlements_response: Optional[shared_requestcatalogsearchservicesearchentitlementsresponse.RequestCatalogSearchServiceSearchEntitlementsResponse] = dataclasses.field(default=None)
    r"""The RequestCatalogSearchServiceSearchEntitlementsResponse message contains a list of results and a nextPageToken if applicable."""
    

