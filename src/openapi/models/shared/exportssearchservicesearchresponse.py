"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .exporter import Exporter, ExporterTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ExportsSearchServiceSearchResponseTypedDict(TypedDict):
    r"""The ExportsSearchServiceSearchResponse message."""
    
    list: NotRequired[Nullable[List[ExporterTypedDict]]]
    r"""The list field."""
    next_page_token: NotRequired[str]
    r"""The nextPageToken field."""
    

class ExportsSearchServiceSearchResponse(BaseModel):
    r"""The ExportsSearchServiceSearchResponse message."""
    
    list: OptionalNullable[List[Exporter]] = UNSET
    r"""The list field."""
    next_page_token: Annotated[Optional[str], pydantic.Field(alias="nextPageToken")] = None
    r"""The nextPageToken field."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["list", "nextPageToken"]
        nullable_fields = ["list"]
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
        
