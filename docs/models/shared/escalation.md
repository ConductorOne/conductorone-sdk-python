# Escalation

The Escalation message.

This message contains a oneof named escalation_policy. Only a single field of the following list may be set at a time:
  - replacePolicy
  - reassignToApprovers



## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `reassign_to_approvers`                                                                    | [OptionalNullable[shared.ReassignToApprovers]](../../models/shared/reassigntoapprovers.md) | :heavy_minus_sign:                                                                         | The ReassignToApprovers message.                                                           |
| `replace_policy`                                                                           | [OptionalNullable[shared.ReplacePolicy]](../../models/shared/replacepolicy.md)             | :heavy_minus_sign:                                                                         | The ReplacePolicy message.                                                                 |
| `escalation_comment`                                                                       | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | The escalationComment field.                                                               |
| `expiration`                                                                               | *Optional[int]*                                                                            | :heavy_minus_sign:                                                                         | The expiration field.                                                                      |