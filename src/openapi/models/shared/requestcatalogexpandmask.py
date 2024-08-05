"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import NotRequired


class RequestCatalogExpandMaskTypedDict(TypedDict):
    r"""The RequestCatalogExpandMask includes the paths in the catalog view to expand in the return value of this call."""
    
    paths: NotRequired[Nullable[List[str]]]
    r"""An array of paths to be expanded in the response. May be any combination of \"*\", \"created_by_user_id\", \"app_ids\", and \"access_entitlements\"."""
    

class RequestCatalogExpandMask(BaseModel):
    r"""The RequestCatalogExpandMask includes the paths in the catalog view to expand in the return value of this call."""
    
    paths: OptionalNullable[List[str]] = UNSET
    r"""An array of paths to be expanded in the response. May be any combination of \"*\", \"created_by_user_id\", \"app_ids\", and \"access_entitlements\"."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["paths"]
        nullable_fields = ["paths"]
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
        
