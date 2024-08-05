"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bundleautomationlastrunstate import BundleAutomationLastRunState, BundleAutomationLastRunStateTypedDict
from .bundleautomationruleentitlement import BundleAutomationRuleEntitlement, BundleAutomationRuleEntitlementTypedDict
from datetime import datetime
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BundleAutomationTypedDict(TypedDict):
    r"""The BundleAutomation message.

    This message contains a oneof named conditions. Only a single field of the following list may be set at a time:
    - entitlements

    """
    
    bundle_automation_last_run_state: NotRequired[BundleAutomationLastRunStateTypedDict]
    r"""The BundleAutomationLastRunState message."""
    bundle_automation_rule_entitlement: NotRequired[Nullable[BundleAutomationRuleEntitlementTypedDict]]
    r"""The BundleAutomationRuleEntitlement message."""
    created_at: NotRequired[datetime]
    deleted_at: NotRequired[datetime]
    request_catalog_id: NotRequired[str]
    r"""The requestCatalogId field."""
    tenant_id: NotRequired[str]
    r"""The tenantId field."""
    updated_at: NotRequired[datetime]
    

class BundleAutomation(BaseModel):
    r"""The BundleAutomation message.

    This message contains a oneof named conditions. Only a single field of the following list may be set at a time:
    - entitlements

    """
    
    bundle_automation_last_run_state: Annotated[Optional[BundleAutomationLastRunState], pydantic.Field(alias="state")] = None
    r"""The BundleAutomationLastRunState message."""
    bundle_automation_rule_entitlement: Annotated[OptionalNullable[BundleAutomationRuleEntitlement], pydantic.Field(alias="entitlements")] = UNSET
    r"""The BundleAutomationRuleEntitlement message."""
    created_at: Annotated[Optional[datetime], pydantic.Field(alias="createdAt")] = None
    deleted_at: Annotated[Optional[datetime], pydantic.Field(alias="deletedAt")] = None
    request_catalog_id: Annotated[Optional[str], pydantic.Field(alias="requestCatalogId")] = None
    r"""The requestCatalogId field."""
    tenant_id: Annotated[Optional[str], pydantic.Field(alias="tenantId")] = None
    r"""The tenantId field."""
    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["BundleAutomationLastRunState", "BundleAutomationRuleEntitlement", "createdAt", "deletedAt", "requestCatalogId", "tenantId", "updatedAt"]
        nullable_fields = ["BundleAutomationRuleEntitlement"]
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
        
