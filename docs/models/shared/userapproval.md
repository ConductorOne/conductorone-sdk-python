# UserApproval

The user approval object describes the approval configuration of a policy step that needs to be approved by a specific list of users.


## Fields

| Field                                                                                               | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `allow_self_approval`                                                                               | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | Configuration to allow self approval of if the user is specified and also the target of the ticket. |
| `user_ids`                                                                                          | list[*str*]                                                                                         | :heavy_minus_sign:                                                                                  | Array of users configured for approval.                                                             |