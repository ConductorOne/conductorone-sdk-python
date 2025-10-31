# TaskAuditPolicyProvisionReassigned

The TaskAuditPolicyProvisionReassigned message.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `new_policy_step_id`                             | *Optional[str]*                                  | :heavy_minus_sign:                               | The newPolicyStepId field.                       |
| `new_users`                                      | List[*str*]                                      | :heavy_minus_sign:                               | The newUsers field.                              |
| `old_policy_step_id`                             | *Optional[str]*                                  | :heavy_minus_sign:                               | The oldPolicyStepId field.                       |
| `users`                                          | List[[shared.User](../../models/shared/user.md)] | :heavy_minus_sign:                               | The users field.                                 |