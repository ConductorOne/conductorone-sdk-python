"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .facetvalue import FacetValue, FacetValueTypedDict
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, TypedDict
from typing_extensions import NotRequired


class FacetValueItemTypedDict(TypedDict):
    r"""The FacetValueItem message."""
    
    values: NotRequired[Nullable[List[FacetValueTypedDict]]]
    r"""An array of facet values."""
    

class FacetValueItem(BaseModel):
    r"""The FacetValueItem message."""
    
    values: OptionalNullable[List[FacetValue]] = UNSET
    r"""An array of facet values."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["values"]
        nullable_fields = ["values"]
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
        
