# WaitInstance

Used by the policy engine to describe an instantiated wait step.

This message contains a oneof named until. Only a single field of the following list may be set at a time:
  - condition


This message contains a oneof named outcome. Only a single field of the following list may be set at a time:
  - succeeded
  - timedOut



## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `condition_succeeded`                                                                          | [OptionalNullable[shared.ConditionSucceeded]](../../models/shared/conditionsucceeded.md)       | :heavy_minus_sign:                                                                             | The ConditionSucceeded message.                                                                |
| `condition_timed_out`                                                                          | [OptionalNullable[shared.ConditionTimedOut]](../../models/shared/conditiontimedout.md)         | :heavy_minus_sign:                                                                             | The ConditionTimedOut message.                                                                 |
| `wait_condition_instance`                                                                      | [OptionalNullable[shared.WaitConditionInstance]](../../models/shared/waitconditioninstance.md) | :heavy_minus_sign:                                                                             | Used by the policy engine to describe an instantiated condition to wait on.                    |
| `comment_on_first_wait`                                                                        | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | The comment to post on first failed check.                                                     |
| `comment_on_timeout`                                                                           | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | The comment to post if we timeout.                                                             |
| `name`                                                                                         | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | The name field.                                                                                |
| `started_waiting_at`                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                           | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `state`                                                                                        | [Optional[shared.WaitInstanceState]](../../models/shared/waitinstancestate.md)                 | :heavy_minus_sign:                                                                             | The state field.                                                                               |
| `timeout`                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                           | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `timeout_duration`                                                                             | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | N/A                                                                                            |