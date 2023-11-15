# CreateAppRequest

The CreateAppRequest message is used to create a new app.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `certify_policy_id`                              | *Optional[str]*                                  | :heavy_minus_sign:                               | Creates the app with this certify policy.        |
| `description`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | Creates the app with this description.           |
| `display_name`                                   | *Optional[str]*                                  | :heavy_minus_sign:                               | Creates the app with this display name.          |
| `grant_policy_id`                                | *Optional[str]*                                  | :heavy_minus_sign:                               | Creates the app with this grant policy.          |
| `monthly_cost_usd`                               | *Optional[float]*                                | :heavy_minus_sign:                               | Creates the app with this monthly cost per seat. |
| `owners`                                         | List[*str*]                                      | :heavy_minus_sign:                               | Creates the app with this array of owners.       |
| `revoke_policy_id`                               | *Optional[str]*                                  | :heavy_minus_sign:                               | Creates the app with this revoke policy.         |