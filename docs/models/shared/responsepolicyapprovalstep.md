# ResponsePolicyApprovalStep

The ResponsePolicyApprovalStep message.

This message contains a oneof named action. Only a single field of the following list may be set at a time:
  - approve
  - deny
  - reassign
  - replacePolicy



## Fields

| Field                                                                                                                      | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `response_policy_approval_replace_policy`                                                                                  | [OptionalNullable[shared.ResponsePolicyApprovalReplacePolicy]](../../models/shared/responsepolicyapprovalreplacepolicy.md) | :heavy_minus_sign:                                                                                                         | The ResponsePolicyApprovalReplacePolicy message.                                                                           |
| `response_policy_approval_step_approve`                                                                                    | [OptionalNullable[shared.ResponsePolicyApprovalStepApprove]](../../models/shared/responsepolicyapprovalstepapprove.md)     | :heavy_minus_sign:                                                                                                         | The ResponsePolicyApprovalStepApprove message.                                                                             |
| `response_policy_approval_step_deny`                                                                                       | [OptionalNullable[shared.ResponsePolicyApprovalStepDeny]](../../models/shared/responsepolicyapprovalstepdeny.md)           | :heavy_minus_sign:                                                                                                         | The ResponsePolicyApprovalStepDeny message.                                                                                |
| `response_policy_approval_step_reassign`                                                                                   | [OptionalNullable[shared.ResponsePolicyApprovalStepReassign]](../../models/shared/responsepolicyapprovalstepreassign.md)   | :heavy_minus_sign:                                                                                                         | The ResponsePolicyApprovalStepReassign message.                                                                            |
| `version`                                                                                                                  | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | version contains the constant value "v1". Future versions of the Webhook Response<br/> will use a different string.        |