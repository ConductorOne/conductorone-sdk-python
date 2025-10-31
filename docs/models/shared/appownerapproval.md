# AppOwnerApproval

App owner approval provides the configuration for an approval step when the app owner is the target.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `allow_self_approval`                                                                                | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | Configuration that allows a user to self approve if they are an app owner during this approval step. |
| `require_distinct_approvers`                                                                         | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | Configuration to require distinct approvers across approval steps of a rule.                         |