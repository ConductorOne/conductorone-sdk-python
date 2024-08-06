"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connector import Connector, ConnectorTypedDict
import pydantic
from sdk.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ConnectorViewTypedDict(TypedDict):
    r"""The ConnectorView object provides a connector response object, as well as JSONPATHs to related objects provided by expanders."""
    
    connector: NotRequired[ConnectorTypedDict]
    r"""A Connector is used to sync objects into Apps"""
    app_path: NotRequired[str]
    r"""JSONPATH expression indicating the location of the App object in the expanded array."""
    users_path: NotRequired[str]
    r"""JSONPATH expression indicating the location of the User object in the expanded array. This is the user that is a direct target of the ticket without a specific relationship to a potentially non-existent app user."""
    

class ConnectorView(BaseModel):
    r"""The ConnectorView object provides a connector response object, as well as JSONPATHs to related objects provided by expanders."""
    
    connector: Optional[Connector] = None
    r"""A Connector is used to sync objects into Apps"""
    app_path: Annotated[Optional[str], pydantic.Field(alias="appPath")] = None
    r"""JSONPATH expression indicating the location of the App object in the expanded array."""
    users_path: Annotated[Optional[str], pydantic.Field(alias="usersPath")] = None
    r"""JSONPATH expression indicating the location of the User object in the expanded array. This is the user that is a direct target of the ticket without a specific relationship to a potentially non-existent app user."""
    