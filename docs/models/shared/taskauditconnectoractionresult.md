# TaskAuditConnectorActionResult

The TaskAuditConnectorActionResult message.

This message contains a oneof named result. Only a single field of the following list may be set at a time:
  - success
  - error
  - cancelled



## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `task_audit_cancelled_result`                                                                        | [OptionalNullable[shared.TaskAuditCancelledResult]](../../models/shared/taskauditcancelledresult.md) | :heavy_minus_sign:                                                                                   | The TaskAuditCancelledResult message.                                                                |
| `task_audit_error_result`                                                                            | [OptionalNullable[shared.TaskAuditErrorResult]](../../models/shared/taskauditerrorresult.md)         | :heavy_minus_sign:                                                                                   | The TaskAuditErrorResult message.                                                                    |
| `task_audit_success_result`                                                                          | [OptionalNullable[shared.TaskAuditSuccessResult]](../../models/shared/taskauditsuccessresult.md)     | :heavy_minus_sign:                                                                                   | The TaskAuditSuccessResult message.                                                                  |
| `app_entitlement_id`                                                                                 | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | The appEntitlementId field.                                                                          |
| `app_id`                                                                                             | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | The appId field.                                                                                     |
| `connector_action_id`                                                                                | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | The connectorActionId field.                                                                         |
| `connector_id`                                                                                       | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | The connectorId field.                                                                               |