"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appentitlement import AppEntitlement, AppEntitlementTypedDict
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AppEntitlementViewTypedDict(TypedDict):
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    
    app_entitlement: NotRequired[AppEntitlementTypedDict]
    r"""The app entitlement represents one permission in a downstream App (SAAS) that can be granted. For example, GitHub Read vs GitHub Write.

    This message contains a oneof named max_grant_duration. Only a single field of the following list may be set at a time:
    - durationUnset
    - durationGrant

    """
    app_path: NotRequired[str]
    r"""JSONPATH expression indicating the location of the App object in the  array."""
    app_resource_path: NotRequired[str]
    r"""JSONPATH expression indicating the location of the App Resource Type object in the expanded array."""
    app_resource_type_path: NotRequired[str]
    r"""JSONPATH expression indicating the location of the App Resource object in the  array."""
    

class AppEntitlementView(BaseModel):
    r"""The app entitlement view contains the serialized app entitlement and paths to objects referenced by the app entitlement."""
    
    app_entitlement: Annotated[Optional[AppEntitlement], pydantic.Field(alias="appEntitlement")] = None
    r"""The app entitlement represents one permission in a downstream App (SAAS) that can be granted. For example, GitHub Read vs GitHub Write.

    This message contains a oneof named max_grant_duration. Only a single field of the following list may be set at a time:
    - durationUnset
    - durationGrant

    """
    app_path: Annotated[Optional[str], pydantic.Field(alias="appPath")] = None
    r"""JSONPATH expression indicating the location of the App object in the  array."""
    app_resource_path: Annotated[Optional[str], pydantic.Field(alias="appResourcePath")] = None
    r"""JSONPATH expression indicating the location of the App Resource Type object in the expanded array."""
    app_resource_type_path: Annotated[Optional[str], pydantic.Field(alias="appResourceTypePath")] = None
    r"""JSONPATH expression indicating the location of the App Resource object in the  array."""
    
