"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import ConfigDict
from sdk.types import BaseModel
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PayloadTypedDict(TypedDict):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    
    at_type: NotRequired[str]
    r"""The type of the serialized message."""
    

class Payload(BaseModel):
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, extra="allow")
    __pydantic_extra__:  Dict[str, Any] = pydantic.Field(init=False)
    
    at_type: Annotated[Optional[str], pydantic.Field(alias="@type")] = None
    r"""The type of the serialized message."""
    
    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value # pyright: ignore[reportIncompatibleVariableOverride]
    

class BodyTypedDict(TypedDict):
    r"""The Body message."""
    
    callback_url: NotRequired[str]
    r"""If your receiver returns HTTP Status Code 202 Accepted, it MUST send its resposne to this URL as a POST
    message body.

    If your receiver returns any other status code, it is expected to not use the callback url.

    This value will match the \"Webhook-Callback-Url\" header.
    """
    event: NotRequired[str]
    r"""The type of event that triggered this Webhook.

    This value will match the \"Webhook-Event\" header.

    The value will be one of:
    - \"c1.webhooks.v1.PayloadTest\" 
    - \"c1.webhooks.v1.PayloadPolicyApprovalStep\" 
    - \"c1.webhooks.v1.PayloadPolicyPostAction\" 
    - \"c1.webhooks.v1.PayloadProvisionStep\" 
    """
    payload: NotRequired[PayloadTypedDict]
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    version: NotRequired[str]
    r"""version contains the constant value \"v1\". Future versions of the Webhook body will use a different string.

    This value will match the \"Webhook-Version\" header.
    """
    webhook_id: NotRequired[str]
    r"""Unique ID for this Webhook. Your receiver should only process this ID once.

    This value will match the \"Webhook-Id\" header.
    """
    

class Body(BaseModel):
    r"""The Body message."""
    
    callback_url: Annotated[Optional[str], pydantic.Field(alias="callbackUrl")] = None
    r"""If your receiver returns HTTP Status Code 202 Accepted, it MUST send its resposne to this URL as a POST
    message body.

    If your receiver returns any other status code, it is expected to not use the callback url.

    This value will match the \"Webhook-Callback-Url\" header.
    """
    event: Optional[str] = None
    r"""The type of event that triggered this Webhook.

    This value will match the \"Webhook-Event\" header.

    The value will be one of:
    - \"c1.webhooks.v1.PayloadTest\" 
    - \"c1.webhooks.v1.PayloadPolicyApprovalStep\" 
    - \"c1.webhooks.v1.PayloadPolicyPostAction\" 
    - \"c1.webhooks.v1.PayloadProvisionStep\" 
    """
    payload: Optional[Payload] = None
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    version: Optional[str] = None
    r"""version contains the constant value \"v1\". Future versions of the Webhook body will use a different string.

    This value will match the \"Webhook-Version\" header.
    """
    webhook_id: Annotated[Optional[str], pydantic.Field(alias="webhookId")] = None
    r"""Unique ID for this Webhook. Your receiver should only process this ID once.

    This value will match the \"Webhook-Id\" header.
    """
    
