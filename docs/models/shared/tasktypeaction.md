# TaskTypeAction

The TaskTypeAction message.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `action_id`                                                                            | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The ID of the action to execute.                                                       |
| `form_values`                                                                          | Dict[str, *Any*]                                                                       | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `outcome`                                                                              | [Optional[shared.TaskTypeActionOutcome]](../../models/shared/tasktypeactionoutcome.md) | :heavy_minus_sign:                                                                     | The outcome field.                                                                     |
| `outcome_time`                                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects)                   | :heavy_minus_sign:                                                                     | N/A                                                                                    |