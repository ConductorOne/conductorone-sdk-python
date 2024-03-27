# WebhookSource

The WebhookSource message.

This message contains a oneof named source. Only a single field of the following list may be set at a time:
  - test
  - policyPostAction
  - approvalStep
  - provisionStep



## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `webhook_source_approval_step`                                                                         | [Optional[shared.WebhookSourceApprovalStep]](../../models/shared/webhooksourceapprovalstep.md)         | :heavy_minus_sign:                                                                                     | The WebhookSourceApprovalStep message.                                                                 |
| `webhook_source_policy_post_action`                                                                    | [Optional[shared.WebhookSourcePolicyPostAction]](../../models/shared/webhooksourcepolicypostaction.md) | :heavy_minus_sign:                                                                                     | The WebhookSourcePolicyPostAction message.                                                             |
| `webhook_source_provision_step`                                                                        | [Optional[shared.WebhookSourceProvisionStep]](../../models/shared/webhooksourceprovisionstep.md)       | :heavy_minus_sign:                                                                                     | The WebhookSourceProvisionStep message.                                                                |
| `webhook_source_test`                                                                                  | [Optional[shared.WebhookSourceTest]](../../models/shared/webhooksourcetest.md)                         | :heavy_minus_sign:                                                                                     | The WebhookSourceTest message.                                                                         |