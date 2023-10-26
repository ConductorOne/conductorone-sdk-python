# ReassignedAction

The ReassignedAction object describes the outcome of a policy step that has been reassigned.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `new_policy_step_id`                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The ID of the policy step that was created as a result of this reassignment. |
| `reassigned_at`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)         | :heavy_minus_sign:                                                           | N/A                                                                          |
| `user_id`                                                                    | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The UserID of the person who reassigned this step.                           |