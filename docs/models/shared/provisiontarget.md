# ProvisionTarget

ProvisionTarget indicates the specific app, app entitlement, and if known, the app user and grant duration of this provision step


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `app_entitlement_id`                                                             | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | The app entitlement that should be provisioned.                                  |
| `app_id`                                                                         | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | The app in which the entitlement should be provisioned                           |
| `app_user_id`                                                                    | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | The app user that should be provisioned. May be unset if the app user is unknown |
| `grant_duration`                                                                 | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | N/A                                                                              |