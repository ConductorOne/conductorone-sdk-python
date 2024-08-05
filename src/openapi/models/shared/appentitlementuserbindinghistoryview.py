"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlementuserbindinghistory import AppEntitlementUserBindingHistory, AppEntitlementUserBindingHistoryTypedDict
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppEntitlementUserBindingHistoryViewTypedDict(TypedDict):
    r"""The AppEntitlementUserBindingHistoryView message."""
    
    app_entitlement_user_binding_history: NotRequired[AppEntitlementUserBindingHistoryTypedDict]
    r"""The AppEntitlementUserBindingHistory message."""
    app_path: NotRequired[str]
    r"""The appPath field."""
    app_user_path: NotRequired[str]
    r"""The appUserPath field."""
    entitlement_path: NotRequired[str]
    r"""The entitlementPath field."""
    

class AppEntitlementUserBindingHistoryView(BaseModel):
    r"""The AppEntitlementUserBindingHistoryView message."""
    
    app_entitlement_user_binding_history: Annotated[Optional[AppEntitlementUserBindingHistory], pydantic.Field(alias="history")] = None
    r"""The AppEntitlementUserBindingHistory message."""
    app_path: Annotated[Optional[str], pydantic.Field(alias="appPath")] = None
    r"""The appPath field."""
    app_user_path: Annotated[Optional[str], pydantic.Field(alias="appUserPath")] = None
    r"""The appUserPath field."""
    entitlement_path: Annotated[Optional[str], pydantic.Field(alias="entitlementPath")] = None
    r"""The entitlementPath field."""
    
