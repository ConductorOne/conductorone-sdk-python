# AppEntitlementUserBindingHistory

The AppEntitlementUserBindingHistory message.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `app_entitlement_id`                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The ID of the app entitlement that the app user has access to        |
| `app_id`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The ID of the app associated with the app entitlement                |
| `app_user_id`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The ID of the app user that has access to the app entitlement        |
| `granted_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `revoked_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |