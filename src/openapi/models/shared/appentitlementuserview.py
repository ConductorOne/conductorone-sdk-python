"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appuserview import AppUserView, AppUserViewTypedDict
from datetime import datetime
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppEntitlementUserViewTypedDict(TypedDict):
    r"""The AppEntitlementUserView (aka grant view) describes the relationship between an app user and an entitlement. They have more recently been referred to as grants."""
    
    app_user_view: NotRequired[AppUserViewTypedDict]
    r"""The AppUserView contains an app user as well as paths for apps, identity users, and last usage in expanded arrays."""
    app_entitlement_user_binding_created_at: NotRequired[datetime]
    app_entitlement_user_binding_deprovision_at: NotRequired[datetime]
    

class AppEntitlementUserView(BaseModel):
    r"""The AppEntitlementUserView (aka grant view) describes the relationship between an app user and an entitlement. They have more recently been referred to as grants."""
    
    app_user_view: Annotated[Optional[AppUserView], pydantic.Field(alias="appUser")] = None
    r"""The AppUserView contains an app user as well as paths for apps, identity users, and last usage in expanded arrays."""
    app_entitlement_user_binding_created_at: Annotated[Optional[datetime], pydantic.Field(alias="appEntitlementUserBindingCreatedAt")] = None
    app_entitlement_user_binding_deprovision_at: Annotated[Optional[datetime], pydantic.Field(alias="appEntitlementUserBindingDeprovisionAt")] = None
    
