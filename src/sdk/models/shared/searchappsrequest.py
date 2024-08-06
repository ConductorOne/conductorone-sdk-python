"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SearchAppsRequestTypedDict(TypedDict):
    r"""Search Apps by a few properties."""
    
    app_ids: NotRequired[Nullable[List[str]]]
    r"""A list of app IDs to restrict the search to."""
    display_name: NotRequired[str]
    r"""Search for apps with a case insensitive match on the display name."""
    exclude_app_ids: NotRequired[Nullable[List[str]]]
    r"""A list of app IDs to remove from the results."""
    only_directories: NotRequired[bool]
    r"""Only return apps which are directories"""
    page_size: NotRequired[int]
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: NotRequired[str]
    r"""The pageToken field."""
    query: NotRequired[str]
    r"""Query the apps with a fuzzy search on display name and description."""
    

class SearchAppsRequest(BaseModel):
    r"""Search Apps by a few properties."""
    
    app_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="appIds")] = UNSET
    r"""A list of app IDs to restrict the search to."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Search for apps with a case insensitive match on the display name."""
    exclude_app_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="excludeAppIds")] = UNSET
    r"""A list of app IDs to remove from the results."""
    only_directories: Annotated[Optional[bool], pydantic.Field(alias="onlyDirectories")] = None
    r"""Only return apps which are directories"""
    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Annotated[Optional[str], pydantic.Field(alias="pageToken")] = None
    r"""The pageToken field."""
    query: Optional[str] = None
    r"""Query the apps with a fuzzy search on display name and description."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["appIds", "displayName", "excludeAppIds", "onlyDirectories", "pageSize", "pageToken", "query"]
        nullable_fields = ["appIds", "excludeAppIds"]
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
        
