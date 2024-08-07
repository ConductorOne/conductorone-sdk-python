"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .provisionpolicy import ProvisionPolicy, ProvisionPolicyTypedDict
from .provisiontarget import ProvisionTarget, ProvisionTargetTypedDict
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ProvisionTypedDict(TypedDict):
    r"""The provision step references a provision policy for this step."""
    
    provision_policy: NotRequired[ProvisionPolicyTypedDict]
    r"""ProvisionPolicy is a oneOf that indicates how a provision step should be processed.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
    - connector
    - manual
    - delegated
    - webhook
    - multiStep
    - externalTicket

    """
    provision_target: NotRequired[ProvisionTargetTypedDict]
    r"""ProvisionTarget indicates the specific app, app entitlement, and if known, the app user and grant duration of this provision step"""
    assigned: NotRequired[bool]
    r"""A field indicating whether this step is assigned."""
    

class Provision(BaseModel):
    r"""The provision step references a provision policy for this step."""
    
    provision_policy: Annotated[Optional[ProvisionPolicy], pydantic.Field(alias="provisionPolicy")] = None
    r"""ProvisionPolicy is a oneOf that indicates how a provision step should be processed.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
    - connector
    - manual
    - delegated
    - webhook
    - multiStep
    - externalTicket

    """
    provision_target: Annotated[Optional[ProvisionTarget], pydantic.Field(alias="provisionTarget")] = None
    r"""ProvisionTarget indicates the specific app, app entitlement, and if known, the app user and grant duration of this provision step"""
    assigned: Optional[bool] = None
    r"""A field indicating whether this step is assigned."""
    
