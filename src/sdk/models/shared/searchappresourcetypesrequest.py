"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SearchAppResourceTypesRequestTypedDict(TypedDict):
    r"""Search for app resources based on some filters."""
    
    app_ids: NotRequired[Nullable[List[str]]]
    r"""A list of app IDs to restrict the search by."""
    app_user_ids: NotRequired[Nullable[List[str]]]
    r"""A list of app user IDs to restrict the search by."""
    exclude_resource_type_ids: NotRequired[Nullable[List[str]]]
    r"""A list of resource type IDs to exclude from the search."""
    exclude_resource_type_trait_ids: NotRequired[Nullable[List[str]]]
    r"""A list of resource type trait IDs to exclude from the search."""
    page_size: NotRequired[int]
    r"""The pageSize where 10 <= pageSize <= 100, default 25."""
    page_token: NotRequired[str]
    r"""The pageToken field."""
    query: NotRequired[str]
    r"""Fuzzy search the display name of resource types."""
    resource_type_ids: NotRequired[Nullable[List[str]]]
    r"""A list of resource type IDs to restrict the search by."""
    resource_type_trait_ids: NotRequired[Nullable[List[str]]]
    r"""A list of resource type trait IDs to restrict the search by."""
    

class SearchAppResourceTypesRequest(BaseModel):
    r"""Search for app resources based on some filters."""
    
    app_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="appIds")] = UNSET
    r"""A list of app IDs to restrict the search by."""
    app_user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="appUserIds")] = UNSET
    r"""A list of app user IDs to restrict the search by."""
    exclude_resource_type_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="excludeResourceTypeIds")] = UNSET
    r"""A list of resource type IDs to exclude from the search."""
    exclude_resource_type_trait_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="excludeResourceTypeTraitIds")] = UNSET
    r"""A list of resource type trait IDs to exclude from the search."""
    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None
    r"""The pageSize where 10 <= pageSize <= 100, default 25."""
    page_token: Annotated[Optional[str], pydantic.Field(alias="pageToken")] = None
    r"""The pageToken field."""
    query: Optional[str] = None
    r"""Fuzzy search the display name of resource types."""
    resource_type_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="resourceTypeIds")] = UNSET
    r"""A list of resource type IDs to restrict the search by."""
    resource_type_trait_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="resourceTypeTraitIds")] = UNSET
    r"""A list of resource type trait IDs to restrict the search by."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["appIds", "appUserIds", "excludeResourceTypeIds", "excludeResourceTypeTraitIds", "pageSize", "pageToken", "query", "resourceTypeIds", "resourceTypeTraitIds"]
        nullable_fields = ["appIds", "appUserIds", "excludeResourceTypeIds", "excludeResourceTypeTraitIds", "resourceTypeIds", "resourceTypeTraitIds"]
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
        
