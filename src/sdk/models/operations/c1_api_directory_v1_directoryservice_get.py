"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from sdk.models.shared import directoryservicegetresponse as shared_directoryservicegetresponse
from sdk.types import BaseModel
from sdk.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class C1APIDirectoryV1DirectoryServiceGetRequestTypedDict(TypedDict):
    app_id: str
    

class C1APIDirectoryV1DirectoryServiceGetRequest(BaseModel):
    app_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    

class C1APIDirectoryV1DirectoryServiceGetResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    directory_service_get_response: NotRequired[shared_directoryservicegetresponse.DirectoryServiceGetResponseTypedDict]
    r"""The Directory Service Get Response returns a directory view with a directory and JSONPATHs indicating the
    location in the expanded array that items are expanded as indicated by the expand mask in the request.
    """
    

class C1APIDirectoryV1DirectoryServiceGetResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    directory_service_get_response: Optional[shared_directoryservicegetresponse.DirectoryServiceGetResponse] = None
    r"""The Directory Service Get Response returns a directory view with a directory and JSONPATHs indicating the
    location in the expanded array that items are expanded as indicated by the expand mask in the request.
    """
    
