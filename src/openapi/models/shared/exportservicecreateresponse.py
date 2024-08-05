"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .exporter import Exporter, ExporterTypedDict
from openapi.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ExportServiceCreateResponseTypedDict(TypedDict):
    r"""The ExportServiceCreateResponse message."""
    
    exporter: NotRequired[ExporterTypedDict]
    r"""The Exporter message.

    This message contains a oneof named export_to. Only a single field of the following list may be set at a time:
    - datasource

    """
    

class ExportServiceCreateResponse(BaseModel):
    r"""The ExportServiceCreateResponse message."""
    
    exporter: Optional[Exporter] = None
    r"""The Exporter message.

    This message contains a oneof named export_to. Only a single field of the following list may be set at a time:
    - datasource

    """
    
