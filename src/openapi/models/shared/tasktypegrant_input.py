"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .taskgrantsource import TaskGrantSource, TaskGrantSourceTypedDict
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class TaskTypeGrantInputTypedDict(TypedDict):
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    
    task_grant_source: NotRequired[TaskGrantSourceTypedDict]
    r"""The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket."""
    

class TaskTypeGrantInput(BaseModel):
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    
    task_grant_source: Annotated[Optional[TaskGrantSource], pydantic.Field(alias="source")] = None
    r"""The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket."""
    
