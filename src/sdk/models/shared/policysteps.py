"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .policystep import PolicyStep, PolicyStepTypedDict
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, TypedDict
from typing_extensions import NotRequired


class PolicyStepsTypedDict(TypedDict):
    r"""The PolicySteps message."""
    
    steps: NotRequired[Nullable[List[PolicyStepTypedDict]]]
    r"""An array of policy steps indicating the processing flow of a policy. These steps are oneOfs, and only one property may be set for each array index at a time."""
    

class PolicySteps(BaseModel):
    r"""The PolicySteps message."""
    
    steps: OptionalNullable[List[PolicyStep]] = UNSET
    r"""An array of policy steps indicating the processing flow of a policy. These steps are oneOfs, and only one property may be set for each array index at a time."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["steps"]
        nullable_fields = ["steps"]
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
        
