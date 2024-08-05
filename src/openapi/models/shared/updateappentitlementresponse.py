"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlementview import AppEntitlementView, AppEntitlementViewTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import ConfigDict, model_serializer
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateAppEntitlementResponseExpandedTypedDict(TypedDict):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    
    at_type: NotRequired[str]
    r"""The type of the serialized message."""
    

class UpdateAppEntitlementResponseExpanded(BaseModel):
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
    

class UpdateAppEntitlementResponseTypedDict(TypedDict):
    r"""The UpdateAppEntitlementResponse message."""
    
    app_entitlement_view: NotRequired[AppEntitlementViewTypedDict]
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    expanded: NotRequired[Nullable[List[UpdateAppEntitlementResponseExpandedTypedDict]]]
    r"""List of related objects"""
    

class UpdateAppEntitlementResponse(BaseModel):
    r"""The UpdateAppEntitlementResponse message."""
    
    app_entitlement_view: Annotated[Optional[AppEntitlementView], pydantic.Field(alias="appEntitlementView")] = None
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    expanded: OptionalNullable[List[UpdateAppEntitlementResponseExpanded]] = UNSET
    r"""List of related objects"""
    
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
        