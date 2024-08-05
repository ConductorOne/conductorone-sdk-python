"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appuserview import AppUserView, AppUserViewTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import ConfigDict, model_serializer
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppUserServiceUpdateResponseExpandedTypedDict(TypedDict):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    
    at_type: NotRequired[str]
    r"""The type of the serialized message."""
    

class AppUserServiceUpdateResponseExpanded(BaseModel):
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
    

class AppUserServiceUpdateResponseTypedDict(TypedDict):
    r"""The AppUserServiceUpdateResponse message."""
    
    app_user_view: NotRequired[AppUserViewTypedDict]
    r"""The AppUserView contains an app user as well as paths for apps, identity users, and last usage in expanded arrays."""
    expanded: NotRequired[Nullable[List[AppUserServiceUpdateResponseExpandedTypedDict]]]
    r"""The expanded field."""
    

class AppUserServiceUpdateResponse(BaseModel):
    r"""The AppUserServiceUpdateResponse message."""
    
    app_user_view: Annotated[Optional[AppUserView], pydantic.Field(alias="appUserView")] = None
    r"""The AppUserView contains an app user as well as paths for apps, identity users, and last usage in expanded arrays."""
    expanded: OptionalNullable[List[AppUserServiceUpdateResponseExpanded]] = UNSET
    r"""The expanded field."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["AppUserView", "expanded"]
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
        
