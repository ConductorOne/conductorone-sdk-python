"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .facetrangeitem import FacetRangeItem, FacetRangeItemTypedDict
from .facetvalueitem import FacetValueItem, FacetValueItemTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class FacetCategoryTypedDict(TypedDict):
    r"""The FacetCategory indicates a grouping of facets by type. For example, facets \"OnePassword\" and \"Okta\" would group under an \"Apps\" category.

    This message contains a oneof named item. Only a single field of the following list may be set at a time:
    - value
    - range

    """
    
    facet_range_item: NotRequired[Nullable[FacetRangeItemTypedDict]]
    r"""The FacetRangeItem message."""
    facet_value_item: NotRequired[Nullable[FacetValueItemTypedDict]]
    r"""The FacetValueItem message."""
    display_name: NotRequired[str]
    r"""The display name of the category."""
    icon_url: NotRequired[str]
    r"""An icon for the category."""
    param: NotRequired[str]
    r"""The param that is being set when checking a facet in this category."""
    

class FacetCategory(BaseModel):
    r"""The FacetCategory indicates a grouping of facets by type. For example, facets \"OnePassword\" and \"Okta\" would group under an \"Apps\" category.

    This message contains a oneof named item. Only a single field of the following list may be set at a time:
    - value
    - range

    """
    
    facet_range_item: Annotated[OptionalNullable[FacetRangeItem], pydantic.Field(alias="range")] = UNSET
    r"""The FacetRangeItem message."""
    facet_value_item: Annotated[OptionalNullable[FacetValueItem], pydantic.Field(alias="value")] = UNSET
    r"""The FacetValueItem message."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The display name of the category."""
    icon_url: Annotated[Optional[str], pydantic.Field(alias="iconUrl")] = None
    r"""An icon for the category."""
    param: Optional[str] = None
    r"""The param that is being set when checking a facet in this category."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["FacetRangeItem", "FacetValueItem", "displayName", "iconUrl", "param"]
        nullable_fields = ["FacetRangeItem", "FacetValueItem"]
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
        