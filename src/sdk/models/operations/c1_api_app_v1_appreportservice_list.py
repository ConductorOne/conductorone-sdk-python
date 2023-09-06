"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import appreportservicelistresponse as shared_appreportservicelistresponse
from typing import Optional



@dataclasses.dataclass
class C1APIAppV1AppReportServiceListRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'app_id', 'style': 'simple', 'explode': False }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    page_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_token', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class C1APIAppV1AppReportServiceListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    app_report_service_list_response: Optional[shared_appreportservicelistresponse.AppReportServiceListResponse] = dataclasses.field(default=None)
    r"""The AppReportServiceListResponse message contains a list of results and a nextPageToken if applicable."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

