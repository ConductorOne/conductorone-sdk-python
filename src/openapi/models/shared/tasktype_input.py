"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tasktypecertify_input import TaskTypeCertifyInput, TaskTypeCertifyInputTypedDict
from .tasktypegrant_input import TaskTypeGrantInput, TaskTypeGrantInputTypedDict
from .tasktypeoffboarding_input import TaskTypeOffboardingInput, TaskTypeOffboardingInputTypedDict
from .tasktyperevoke_input import TaskTypeRevokeInput, TaskTypeRevokeInputTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import Annotated, NotRequired


class TaskTypeInputTypedDict(TypedDict):
    r"""Task Type provides configuration for the type of task: certify, grant, or revoke

    This message contains a oneof named task_type. Only a single field of the following list may be set at a time:
    - grant
    - revoke
    - certify
    - offboarding

    """
    
    task_type_certify: NotRequired[Nullable[TaskTypeCertifyInputTypedDict]]
    r"""The TaskTypeCertify message indicates that a task is a certify task and all related details."""
    task_type_grant: NotRequired[Nullable[TaskTypeGrantInputTypedDict]]
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    task_type_offboarding: NotRequired[Nullable[TaskTypeOffboardingInputTypedDict]]
    r"""The TaskTypeOffboarding message."""
    task_type_revoke: NotRequired[Nullable[TaskTypeRevokeInputTypedDict]]
    r"""The TaskTypeRevoke message indicates that a task is a revoke task and all related details."""
    

class TaskTypeInput(BaseModel):
    r"""Task Type provides configuration for the type of task: certify, grant, or revoke

    This message contains a oneof named task_type. Only a single field of the following list may be set at a time:
    - grant
    - revoke
    - certify
    - offboarding

    """
    
    task_type_certify: Annotated[OptionalNullable[TaskTypeCertifyInput], pydantic.Field(alias="certify")] = UNSET
    r"""The TaskTypeCertify message indicates that a task is a certify task and all related details."""
    task_type_grant: Annotated[OptionalNullable[TaskTypeGrantInput], pydantic.Field(alias="grant")] = UNSET
    r"""The TaskTypeGrant message indicates that a task is a grant task and all related details."""
    task_type_offboarding: Annotated[OptionalNullable[TaskTypeOffboardingInput], pydantic.Field(alias="offboarding")] = UNSET
    r"""The TaskTypeOffboarding message."""
    task_type_revoke: Annotated[OptionalNullable[TaskTypeRevokeInput], pydantic.Field(alias="revoke")] = UNSET
    r"""The TaskTypeRevoke message indicates that a task is a revoke task and all related details."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["TaskTypeCertify", "TaskTypeGrant", "TaskTypeOffboarding", "TaskTypeRevoke"]
        nullable_fields = ["TaskTypeCertify", "TaskTypeGrant", "TaskTypeOffboarding", "TaskTypeRevoke"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        