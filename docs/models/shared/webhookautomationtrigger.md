# WebhookAutomationTrigger

The WebhookAutomationTrigger message.

This message contains a oneof named auth_config. Only a single field of the following list may be set at a time:
  - jwt
  - hmac



## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `webhook_listener_auth_hmac`                                                                       | [OptionalNullable[shared.WebhookListenerAuthHMAC]](../../models/shared/webhooklistenerauthhmac.md) | :heavy_minus_sign:                                                                                 | The WebhookListenerAuthHMAC message.                                                               |
| `webhook_listener_auth_jwt`                                                                        | [OptionalNullable[shared.WebhookListenerAuthJWT]](../../models/shared/webhooklistenerauthjwt.md)   | :heavy_minus_sign:                                                                                 | The WebhookListenerAuthJWT message.                                                                |
| `listener_id`                                                                                      | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | Optional existing listener ID (hidden field from frontend)                                         |