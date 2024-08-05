"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlementview import AppEntitlementView, AppEntitlementViewTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import ConfigDict, model_serializer
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListAppEntitlementsResponseExpandedTypedDict(TypedDict):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    
    at_type: NotRequired[str]
    r"""The type of the serialized message."""
    

class ListAppEntitlementsResponseExpanded(BaseModel):
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
    

class ListAppEntitlementsResponseTypedDict(TypedDict):
    r"""The ListAppEntitlementsResponse message contains a list of results and a nextPageToken if applicable."""
    
    expanded: NotRequired[Nullable[List[ListAppEntitlementsResponseExpandedTypedDict]]]
    r"""List of related objects"""
    list: NotRequired[Nullable[List[AppEntitlementViewTypedDict]]]
    r"""The list of results containing up to X results, where X is the page size defined in the request."""
    next_page_token: NotRequired[str]
    r"""The nextPageToken is shown for the next page if the number of results is larger than the max page size. The server returns one page of results and the nextPageToken until all results are retreived. To retrieve the next page, use the same request and append a pageToken field with the value of nextPageToken shown on the previous page."""
    

class ListAppEntitlementsResponse(BaseModel):
    r"""The ListAppEntitlementsResponse message contains a list of results and a nextPageToken if applicable."""
    
    expanded: OptionalNullable[List[ListAppEntitlementsResponseExpanded]] = UNSET
    r"""List of related objects"""
    list: OptionalNullable[List[AppEntitlementView]] = UNSET
    r"""The list of results containing up to X results, where X is the page size defined in the request."""
    next_page_token: Annotated[Optional[str], pydantic.Field(alias="nextPageToken")] = None
    r"""The nextPageToken is shown for the next page if the number of results is larger than the max page size. The server returns one page of results and the nextPageToken until all results are retreived. To retrieve the next page, use the same request and append a pageToken field with the value of nextPageToken shown on the previous page."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expanded", "list", "nextPageToken"]
        nullable_fields = ["expanded", "list"]
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
        
