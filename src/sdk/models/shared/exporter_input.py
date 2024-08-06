"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .exporttodatasource import ExportToDatasource, ExportToDatasourceTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ExporterInputTypedDict(TypedDict):
    r"""The Exporter message.

    This message contains a oneof named export_to. Only a single field of the following list may be set at a time:
    - datasource

    """
    
    export_to_datasource: NotRequired[Nullable[ExportToDatasourceTypedDict]]
    r"""The ExportToDatasource message."""
    display_name: NotRequired[str]
    r"""The displayName field."""
    

class ExporterInput(BaseModel):
    r"""The Exporter message.

    This message contains a oneof named export_to. Only a single field of the following list may be set at a time:
    - datasource

    """
    
    export_to_datasource: Annotated[OptionalNullable[ExportToDatasource], pydantic.Field(alias="datasource")] = UNSET
    r"""The ExportToDatasource message."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The displayName field."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ExportToDatasource", "displayName"]
        nullable_fields = ["ExportToDatasource"]
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
        