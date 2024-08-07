"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connectorexpandmask import ConnectorExpandMask, ConnectorExpandMaskTypedDict
import pydantic
from pydantic import ConfigDict, model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ConnectorServiceCreateRequestConfigTypedDict(TypedDict):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    
    at_type: NotRequired[str]
    r"""The type of the serialized message."""
    

class ConnectorServiceCreateRequestConfig(BaseModel):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    at_type: Annotated[Optional[str], pydantic.Field(alias="@type")] = None
    r"""The type of the serialized message."""
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    

class ConnectorServiceCreateRequestTypedDict(TypedDict):
    r"""The ConnectorServiceCreateRequest message."""
    
    connector_expand_mask: NotRequired[ConnectorExpandMaskTypedDict]
    r"""The ConnectorExpandMask is used to expand related objects on a connector."""
    catalog_id: NotRequired[str]
    r"""The catalogId field."""
    config: NotRequired[ConnectorServiceCreateRequestConfigTypedDict]
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    description: NotRequired[str]
    r"""The description field."""
    user_ids: NotRequired[Nullable[List[str]]]
    r"""The userIds field."""
    

class ConnectorServiceCreateRequest(BaseModel):
    r"""The ConnectorServiceCreateRequest message."""
    
    connector_expand_mask: Annotated[Optional[ConnectorExpandMask], pydantic.Field(alias="expandMask")] = None
    r"""The ConnectorExpandMask is used to expand related objects on a connector."""
    catalog_id: Annotated[Optional[str], pydantic.Field(alias="catalogId")] = None
    r"""The catalogId field."""
    config: Optional[ConnectorServiceCreateRequestConfig] = None
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    description: Optional[str] = None
    r"""The description field."""
    user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="userIds")] = UNSET
    r"""The userIds field."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ConnectorExpandMask", "catalogId", "config", "description", "userIds"]
        nullable_fields = ["userIds"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        
