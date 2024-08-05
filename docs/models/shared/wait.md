# Wait

Define a Wait step for a policy to wait on a condition to be met.

This message contains a oneof named until. Only a single field of the following list may be set at a time:
  - condition



## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `wait_condition`                                                               | [OptionalNullable[shared.WaitCondition]](../../models/shared/waitcondition.md) | :heavy_minus_sign:                                                             | The WaitCondition message.                                                     |
| `comment_on_first_wait`                                                        | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The comment to post on first failed check.                                     |
| `comment_on_timeout`                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The comment to post if we timeout.                                             |
| `name`                                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The name of our condition to show on the task details page                     |
| `timeout_duration`                                                             | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            |