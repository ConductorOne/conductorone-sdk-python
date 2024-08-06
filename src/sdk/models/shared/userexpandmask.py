"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, TypedDict
from typing_extensions import NotRequired


class UserExpandMaskTypedDict(TypedDict):
    r"""The user expand mask is used to indicate which related objects should be expanded in the response.
    The supported paths are 'role_ids', 'manager_ids', 'delegated_user_id', 'directory_ids', and '*'.
    """
    
    paths: NotRequired[Nullable[List[str]]]
    r"""An array of paths to be expanded in the response."""
    

class UserExpandMask(BaseModel):
    r"""The user expand mask is used to indicate which related objects should be expanded in the response.
    The supported paths are 'role_ids', 'manager_ids', 'delegated_user_id', 'directory_ids', and '*'.
    """
    
    paths: OptionalNullable[List[str]] = UNSET
    r"""An array of paths to be expanded in the response."""
    
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

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
