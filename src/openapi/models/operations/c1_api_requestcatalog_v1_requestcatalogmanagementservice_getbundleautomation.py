"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from openapi.models.shared import bundleautomation as shared_bundleautomation
from openapi.types import BaseModel
from openapi.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIRequestcatalogV1RequestCatalogManagementServiceGetBundleAutomationRequestTypedDict(TypedDict):
    request_catalog_id: str
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceGetBundleAutomationRequest(BaseModel):
    request_catalog_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceGetBundleAutomationResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    bundle_automation: NotRequired[shared_bundleautomation.BundleAutomationTypedDict]
    r"""Successful response"""
    

class C1APIRequestcatalogV1RequestCatalogManagementServiceGetBundleAutomationResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    bundle_automation: Optional[shared_bundleautomation.BundleAutomation] = None
    r"""Successful response"""
    