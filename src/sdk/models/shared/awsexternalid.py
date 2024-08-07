"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AWSExternalIDTypedDict(TypedDict):
    r"""The AWSExternalID message."""
    
    external_id: NotRequired[str]
    r"""The externalId field."""
    

class AWSExternalID(BaseModel):
    r"""The AWSExternalID message."""
    
    external_id: Annotated[Optional[str], pydantic.Field(alias="externalId")] = None
    r"""The externalId field."""
    
