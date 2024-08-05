"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from openapi.types import BaseModel
from typing import TypedDict


class ForceSyncRequestTypedDict(TypedDict):
    r"""Signal the connector to start syncing. This puts the sync on the queue. It does not guarantee immediate sync. Long syncs still take minutes to hours."""
    
    

class ForceSyncRequest(BaseModel):
    r"""Signal the connector to start syncing. This puts the sync on the queue. It does not guarantee immediate sync. Long syncs still take minutes to hours."""
    
    
