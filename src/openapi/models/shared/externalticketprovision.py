"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ExternalTicketProvisionTypedDict(TypedDict):
    r"""This provision step indicates that we should check an external ticket to provision this entitlement"""
    
    app_id: NotRequired[str]
    r"""The appId field."""
    connector_id: NotRequired[str]
    r"""The connectorId field."""
    external_ticket_provisioner_config_id: NotRequired[str]
    r"""The externalTicketProvisionerConfigId field."""
    

class ExternalTicketProvision(BaseModel):
    r"""This provision step indicates that we should check an external ticket to provision this entitlement"""
    
    app_id: Annotated[Optional[str], pydantic.Field(alias="appId")] = None
    r"""The appId field."""
    connector_id: Annotated[Optional[str], pydantic.Field(alias="connectorId")] = None
    r"""The connectorId field."""
    external_ticket_provisioner_config_id: Annotated[Optional[str], pydantic.Field(alias="externalTicketProvisionerConfigId")] = None
    r"""The externalTicketProvisionerConfigId field."""
    