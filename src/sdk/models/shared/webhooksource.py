"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhooksourceapprovalstep import WebhookSourceApprovalStep, WebhookSourceApprovalStepTypedDict
from .webhooksourcepolicypostaction import WebhookSourcePolicyPostAction, WebhookSourcePolicyPostActionTypedDict
from .webhooksourceprovisionstep import WebhookSourceProvisionStep, WebhookSourceProvisionStepTypedDict
from .webhooksourcetest import WebhookSourceTest, WebhookSourceTestTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import TypedDict
from typing_extensions import Annotated, NotRequired


class WebhookSourceTypedDict(TypedDict):
    r"""The WebhookSource message.

    This message contains a oneof named source. Only a single field of the following list may be set at a time:
    - test
    - policyPostAction
    - approvalStep
    - provisionStep

    """
    
    webhook_source_approval_step: NotRequired[Nullable[WebhookSourceApprovalStepTypedDict]]
    r"""The WebhookSourceApprovalStep message."""
    webhook_source_policy_post_action: NotRequired[Nullable[WebhookSourcePolicyPostActionTypedDict]]
    r"""The WebhookSourcePolicyPostAction message."""
    webhook_source_provision_step: NotRequired[Nullable[WebhookSourceProvisionStepTypedDict]]
    r"""The WebhookSourceProvisionStep message."""
    webhook_source_test: NotRequired[Nullable[WebhookSourceTestTypedDict]]
    r"""The WebhookSourceTest message."""
    

class WebhookSource(BaseModel):
    r"""The WebhookSource message.

    This message contains a oneof named source. Only a single field of the following list may be set at a time:
    - test
    - policyPostAction
    - approvalStep
    - provisionStep

    """
    
    webhook_source_approval_step: Annotated[OptionalNullable[WebhookSourceApprovalStep], pydantic.Field(alias="approvalStep")] = UNSET
    r"""The WebhookSourceApprovalStep message."""
    webhook_source_policy_post_action: Annotated[OptionalNullable[WebhookSourcePolicyPostAction], pydantic.Field(alias="policyPostAction")] = UNSET
    r"""The WebhookSourcePolicyPostAction message."""
    webhook_source_provision_step: Annotated[OptionalNullable[WebhookSourceProvisionStep], pydantic.Field(alias="provisionStep")] = UNSET
    r"""The WebhookSourceProvisionStep message."""
    webhook_source_test: Annotated[OptionalNullable[WebhookSourceTest], pydantic.Field(alias="test")] = UNSET
    r"""The WebhookSourceTest message."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["WebhookSourceApprovalStep", "WebhookSourcePolicyPostAction", "WebhookSourceProvisionStep", "WebhookSourceTest"]
        nullable_fields = ["WebhookSourceApprovalStep", "WebhookSourcePolicyPostAction", "WebhookSourceProvisionStep", "WebhookSourceTest"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        