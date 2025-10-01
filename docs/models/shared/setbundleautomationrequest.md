# SetBundleAutomationRequest

The SetBundleAutomationRequest message.

This message contains a oneof named conditions. Only a single field of the following list may be set at a time:
  - entitlements



## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `bundle_automation_rule_entitlement`                                                                               | [OptionalNullable[shared.BundleAutomationRuleEntitlement]](../../models/shared/bundleautomationruleentitlement.md) | :heavy_minus_sign:                                                                                                 | The BundleAutomationRuleEntitlement message.                                                                       |
| `create_tasks`                                                                                                     | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | The createTasks field.                                                                                             |
| `disable_circuit_breaker`                                                                                          | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | The disableCircuitBreaker field.                                                                                   |
| `enabled`                                                                                                          | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | The enabled field.                                                                                                 |