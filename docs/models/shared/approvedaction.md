# ApprovedAction

The approved action indicates that the approvalinstance had an outcome of approved.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `approved_at`                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                   | :heavy_minus_sign:                                                                     | N/A                                                                                    |
| `entitlements`                                                                         | list[[AppEntitlementReference](../../models/shared/appentitlementreference.md)]        | :heavy_minus_sign:                                                                     | The entitlements that were approved. This will only ever be a list of one entitlement. |
| `user_id`                                                                              | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | The UserID that approved this step.                                                    |