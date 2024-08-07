"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlementreference import AppEntitlementReference, AppEntitlementReferenceTypedDict
from datetime import datetime
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CompletedActionTypedDict(TypedDict):
    r"""The outcome of a provision instance that has been completed succesfully."""
    
    completed_at: NotRequired[datetime]
    entitlements: NotRequired[Nullable[List[AppEntitlementReferenceTypedDict]]]
    r"""The list of entitlements that were provisioned. This is leftover from an older design, and is only ever going to be a single entitlement."""
    user_id: NotRequired[str]
    r"""The UserID of who completed provisioning. For connector provisioning this is the system user id, for manual provisioning this is who clicked \"provision complete\" """
    

class CompletedAction(BaseModel):
    r"""The outcome of a provision instance that has been completed succesfully."""
    
    completed_at: Annotated[Optional[datetime], pydantic.Field(alias="completedAt")] = None
    entitlements: OptionalNullable[List[AppEntitlementReference]] = UNSET
    r"""The list of entitlements that were provisioned. This is leftover from an older design, and is only ever going to be a single entitlement."""
    user_id: Annotated[Optional[str], pydantic.Field(alias="userId")] = None
    r"""The UserID of who completed provisioning. For connector provisioning this is the system user id, for manual provisioning this is who clicked \"provision complete\" """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["completedAt", "entitlements", "userId"]
        nullable_fields = ["entitlements"]
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
        
