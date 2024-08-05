"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlementref import AppEntitlementRef, AppEntitlementRefTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import Annotated, NotRequired


class BundleAutomationRuleEntitlementTypedDict(TypedDict):
    r"""The BundleAutomationRuleEntitlement message."""
    
    entitlement_refs: NotRequired[Nullable[List[AppEntitlementRefTypedDict]]]
    r"""The entitlementRefs field."""
    

class BundleAutomationRuleEntitlement(BaseModel):
    r"""The BundleAutomationRuleEntitlement message."""
    
    entitlement_refs: Annotated[OptionalNullable[List[AppEntitlementRef]], pydantic.Field(alias="entitlementRefs")] = UNSET
    r"""The entitlementRefs field."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["entitlementRefs"]
        nullable_fields = ["entitlementRefs"]
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
        
