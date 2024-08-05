# AppAccessRequestDefaults1

The AppAccessRequestDefaults message.

This message contains a oneof named max_grant_duration. Only a single field of the following list may be set at a time:
  - durationUnset
  - durationGrant



## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `catalog_ids`                                                                            | List[*str*]                                                                              | :heavy_minus_sign:                                                                       | The request catalog ids for the app access request rule.                                 |
| `defaults_enabled`                                                                       | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | If true the app level request configuration will be applied to specified resource types. |
| `duration_grant`                                                                         | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `duration_unset`                                                                         | [OptionalNullable[shared.DurationUnset]](../../models/shared/durationunset.md)           | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `emergency_grant_enabled`                                                                | *Optional[bool]*                                                                         | :heavy_minus_sign:                                                                       | If emergency grants are enabled for this app access request rule.                        |
| `emergency_grant_policy_id`                                                              | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | The policy id for the emergency grant policy.                                            |
| `request_policy_id`                                                                      | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | The requestPolicyId field.                                                               |
| `resource_type_ids`                                                                      | List[*str*]                                                                              | :heavy_minus_sign:                                                                       | The app resource type ids for which the app access request defaults are applied.         |
| `state`                                                                                  | [Optional[shared.State]](../../models/shared/state.md)                                   | :heavy_minus_sign:                                                                       | The last applied state of the app access request defaults.                               |