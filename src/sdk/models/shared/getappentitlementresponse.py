"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlementview import AppEntitlementView, AppEntitlementViewTypedDict
import pydantic
from pydantic import ConfigDict, model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetAppEntitlementResponseExpandedTypedDict(TypedDict):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    
    at_type: NotRequired[str]
    r"""The type of the serialized message."""
    

class GetAppEntitlementResponseExpanded(BaseModel):
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
    

class GetAppEntitlementResponseTypedDict(TypedDict):
    r"""The get app entitlement response returns an entitlement view containing paths in the expanded array for the objects expanded as indicated by the expand mask in the request."""
    
    app_entitlement_view: NotRequired[AppEntitlementViewTypedDict]
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    expanded: NotRequired[Nullable[List[GetAppEntitlementResponseExpandedTypedDict]]]
    r"""List of serialized related objects."""
    

class GetAppEntitlementResponse(BaseModel):
    r"""The get app entitlement response returns an entitlement view containing paths in the expanded array for the objects expanded as indicated by the expand mask in the request."""
    
    app_entitlement_view: Annotated[Optional[AppEntitlementView], pydantic.Field(alias="appEntitlementView")] = None
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    expanded: OptionalNullable[List[GetAppEntitlementResponseExpanded]] = UNSET
    r"""List of serialized related objects."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["AppEntitlementView", "expanded"]
        nullable_fields = ["expanded"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
