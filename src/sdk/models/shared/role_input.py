"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class RoleInputTypedDict(TypedDict):
    r"""Role is a role that can be assigned to a user in ConductorOne."""
    
    display_name: NotRequired[str]
    r"""The display name of the role."""
    permissions: NotRequired[Nullable[List[str]]]
    r"""The list of permissions this role has."""
    service_roles: NotRequired[Nullable[List[str]]]
    r"""The list of serviceRoles that this role has."""
    

class RoleInput(BaseModel):
    r"""Role is a role that can be assigned to a user in ConductorOne."""
    
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The display name of the role."""
    permissions: OptionalNullable[List[str]] = UNSET
    r"""The list of permissions this role has."""
    service_roles: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="serviceRoles")] = UNSET
    r"""The list of serviceRoles that this role has."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["displayName", "permissions", "serviceRoles"]
        nullable_fields = ["permissions", "serviceRoles"]
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
        
