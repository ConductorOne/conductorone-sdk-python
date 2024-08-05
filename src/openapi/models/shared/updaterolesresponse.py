"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .role import Role, RoleTypedDict
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class UpdateRolesResponseTypedDict(TypedDict):
    r"""UpdateRolesResponse is the response message containing the updated role."""
    
    role: NotRequired[RoleTypedDict]
    r"""Role is a role that can be assigned to a user in ConductorOne."""
    

class UpdateRolesResponse(BaseModel):
    r"""UpdateRolesResponse is the response message containing the updated role."""
    
    role: Optional[Role] = None
    r"""Role is a role that can be assigned to a user in ConductorOne."""
    
