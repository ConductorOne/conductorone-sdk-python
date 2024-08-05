"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .app import AppInput, AppInputTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateAppRequestTypedDict(TypedDict):
    r"""The UpdateAppRequest message contains the app to update and the fields to update."""
    
    app: NotRequired[AppInputTypedDict]
    r"""The App object provides all of the details for an app, as well as some configuration."""
    update_mask: NotRequired[Nullable[str]]
    

class UpdateAppRequest(BaseModel):
    r"""The UpdateAppRequest message contains the app to update and the fields to update."""
    
    app: Optional[AppInput] = None
    r"""The App object provides all of the details for an app, as well as some configuration."""
    update_mask: Annotated[OptionalNullable[str], pydantic.Field(alias="updateMask")] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["App", "updateMask"]
        nullable_fields = ["updateMask"]
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
        