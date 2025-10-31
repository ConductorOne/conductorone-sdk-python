# WebhookSource

The WebhookSource message.

This message contains a oneof named source. Only a single field of the following list may be set at a time:
  - test
  - policyPostAction
  - approvalStep
  - provisionStep
  - workflowStep



## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `webhook_source_approval_step`                                                                                 | [OptionalNullable[shared.WebhookSourceApprovalStep]](../../models/shared/webhooksourceapprovalstep.md)         | :heavy_minus_sign:                                                                                             | The WebhookSourceApprovalStep message.                                                                         |
| `webhook_source_policy_post_action`                                                                            | [OptionalNullable[shared.WebhookSourcePolicyPostAction]](../../models/shared/webhooksourcepolicypostaction.md) | :heavy_minus_sign:                                                                                             | The WebhookSourcePolicyPostAction message.                                                                     |
| `webhook_source_provision_step`                                                                                | [OptionalNullable[shared.WebhookSourceProvisionStep]](../../models/shared/webhooksourceprovisionstep.md)       | :heavy_minus_sign:                                                                                             | The WebhookSourceProvisionStep message.                                                                        |
| `webhook_source_test`                                                                                          | [OptionalNullable[shared.WebhookSourceTest]](../../models/shared/webhooksourcetest.md)                         | :heavy_minus_sign:                                                                                             | The WebhookSourceTest message.                                                                                 |
| `webhook_source_workflow_step`                                                                                 | [OptionalNullable[shared.WebhookSourceWorkflowStep]](../../models/shared/webhooksourceworkflowstep.md)         | :heavy_minus_sign:                                                                                             | The WebhookSourceWorkflowStep message.                                                                         |