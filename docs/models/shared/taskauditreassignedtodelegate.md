# TaskAuditReassignedToDelegate

The TaskAuditReassignedToDelegate message.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `user`                                                                                  | [Optional[shared.User]](../../models/shared/user.md)                                    | :heavy_minus_sign:                                                                      | The User object provides all of the details for an user, as well as some configuration. |
| `user1`                                                                                 | [Optional[shared.User]](../../models/shared/user.md)                                    | :heavy_minus_sign:                                                                      | The User object provides all of the details for an user, as well as some configuration. |
| `delegated_assignee_user_id`                                                            | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | The delegatedAssigneeUserId field.                                                      |
| `original_assignee_user_id`                                                             | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | The originalAssigneeUserId field.                                                       |