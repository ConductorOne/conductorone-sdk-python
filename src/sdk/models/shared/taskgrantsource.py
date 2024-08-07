"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TaskGrantSourceTypedDict(TypedDict):
    r"""The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket."""
    
    external_url: NotRequired[str]
    r"""The external url source of the grant ticket."""
    integration_id: NotRequired[str]
    r"""The integration id for the source of tickets."""
    request_id: NotRequired[str]
    r"""the request id for the grant ticket if the source is external"""
    

class TaskGrantSource(BaseModel):
    r"""The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket."""
    
    external_url: Annotated[Optional[str], pydantic.Field(alias="externalUrl")] = None
    r"""The external url source of the grant ticket."""
    integration_id: Annotated[Optional[str], pydantic.Field(alias="integrationId")] = None
    r"""The integration id for the source of tickets."""
    request_id: Annotated[Optional[str], pydantic.Field(alias="requestId")] = None
    r"""the request id for the grant ticket if the source is external"""
    
