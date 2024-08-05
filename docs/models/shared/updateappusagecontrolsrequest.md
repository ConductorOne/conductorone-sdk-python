# UpdateAppUsageControlsRequest

The UpdateAppUsageControlsRequest message contains the AppUsageControls object to update and the update mask.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `app_usage_controls`                                                            | [Optional[shared.AppUsageControls]](../../models/shared/appusagecontrols.md)    | :heavy_minus_sign:                                                              | The AppUsageControls object describes some peripheral configuration for an app. |
| `update_mask`                                                                   | *OptionalNullable[str]*                                                         | :heavy_minus_sign:                                                              | N/A                                                                             |