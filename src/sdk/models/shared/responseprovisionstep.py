"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .responseprovisionstepcomplete import ResponseProvisionStepComplete, ResponseProvisionStepCompleteTypedDict
from .responseprovisionsteperrored import ResponseProvisionStepErrored, ResponseProvisionStepErroredTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ResponseProvisionStepTypedDict(TypedDict):
    r"""The ResponseProvisionStep message.

    This message contains a oneof named outcome. Only a single field of the following list may be set at a time:
    - complete
    - errored

    """
    
    response_provision_step_complete: NotRequired[Nullable[ResponseProvisionStepCompleteTypedDict]]
    r"""The ResponseProvisionStepComplete message."""
    response_provision_step_errored: NotRequired[Nullable[ResponseProvisionStepErroredTypedDict]]
    r"""The ResponseProvisionStepErrored message."""
    version: NotRequired[str]
    r"""version contains the constant value \"v1\". Future versions of the Webhook Response
    will use a different string.
    """
    

class ResponseProvisionStep(BaseModel):
    r"""The ResponseProvisionStep message.

    This message contains a oneof named outcome. Only a single field of the following list may be set at a time:
    - complete
    - errored

    """
    
    response_provision_step_complete: Annotated[OptionalNullable[ResponseProvisionStepComplete], pydantic.Field(alias="complete")] = UNSET
    r"""The ResponseProvisionStepComplete message."""
    response_provision_step_errored: Annotated[OptionalNullable[ResponseProvisionStepErrored], pydantic.Field(alias="errored")] = UNSET
    r"""The ResponseProvisionStepErrored message."""
    version: Optional[str] = None
    r"""version contains the constant value \"v1\". Future versions of the Webhook Response
    will use a different string.
    """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ResponseProvisionStepComplete", "ResponseProvisionStepErrored", "version"]
        nullable_fields = ["ResponseProvisionStepComplete", "ResponseProvisionStepErrored"]
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
        
