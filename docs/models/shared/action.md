# Action

The Action message.

This message contains a oneof named target. Only a single field of the following list may be set at a time:
  - automation



## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `action_target_automation`                                                                       | [OptionalNullable[shared.ActionTargetAutomation]](../../models/shared/actiontargetautomation.md) | :heavy_minus_sign:                                                                               | The ActionTargetAutomation message.                                                              |