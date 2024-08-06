"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlementref import AppEntitlementRef, AppEntitlementRefTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, TypedDict
from typing_extensions import Annotated, NotRequired


class RequestCatalogManagementServiceRemoveAccessEntitlementsRequestTypedDict(TypedDict):
    r"""The RequestCatalogManagementServiceRemoveAccessEntitlementsRequest message is used to remove access entitlements from a request catalog.
    The access entitlements are used to determine which users can view the request catalog.
    """
    
    access_entitlements: NotRequired[Nullable[List[AppEntitlementRefTypedDict]]]
    r"""The list of access entitlements to remove from the catalog."""
    

class RequestCatalogManagementServiceRemoveAccessEntitlementsRequest(BaseModel):
    r"""The RequestCatalogManagementServiceRemoveAccessEntitlementsRequest message is used to remove access entitlements from a request catalog.
    The access entitlements are used to determine which users can view the request catalog.
    """
    
    access_entitlements: Annotated[OptionalNullable[List[AppEntitlementRef]], pydantic.Field(alias="accessEntitlements")] = UNSET
    r"""The list of access entitlements to remove from the catalog."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["accessEntitlements"]
        nullable_fields = ["accessEntitlements"]
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
        
