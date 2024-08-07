"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhook_input import WebhookInput, WebhookInputTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class WebhooksServiceUpdateRequestTypedDict(TypedDict):
    r"""The WebhooksServiceUpdateRequest message contains the webhook object to update and a field mask to indicate which fields to update. It uses URL value for input."""
    
    webhook: NotRequired[WebhookInputTypedDict]
    r"""The Webhook message."""
    update_mask: NotRequired[Nullable[str]]
    

class WebhooksServiceUpdateRequest(BaseModel):
    r"""The WebhooksServiceUpdateRequest message contains the webhook object to update and a field mask to indicate which fields to update. It uses URL value for input."""
    
    webhook: Optional[WebhookInput] = None
    r"""The Webhook message."""
    update_mask: Annotated[OptionalNullable[str], pydantic.Field(alias="updateMask")] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["Webhook", "updateMask"]
        nullable_fields = ["updateMask"]
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
        
