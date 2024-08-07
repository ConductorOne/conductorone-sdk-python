"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AttributeValueTypedDict(TypedDict):
    r"""AttributeValue is the value of an attribute of a defined type."""
    
    attribute_type_id: NotRequired[str]
    r"""The ID of the AttributeType that this AttributeValue belongs to."""
    created_at: NotRequired[datetime]
    deleted_at: NotRequired[datetime]
    id: NotRequired[str]
    r"""The ID of the AttributeValue."""
    updated_at: NotRequired[datetime]
    value: NotRequired[str]
    r"""The value of the AttributeValue. This is the string that will be displayed to the user."""
    

class AttributeValue(BaseModel):
    r"""AttributeValue is the value of an attribute of a defined type."""
    
    attribute_type_id: Annotated[Optional[str], pydantic.Field(alias="attributeTypeId")] = None
    r"""The ID of the AttributeType that this AttributeValue belongs to."""
    created_at: Annotated[Optional[datetime], pydantic.Field(alias="createdAt")] = None
    deleted_at: Annotated[Optional[datetime], pydantic.Field(alias="deletedAt")] = None
    id: Optional[str] = None
    r"""The ID of the AttributeValue."""
    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
    value: Optional[str] = None
    r"""The value of the AttributeValue. This is the string that will be displayed to the user."""
    
