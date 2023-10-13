# GetAppUsageControlsResponse

The GetAppUsageControlsResponse message contains the retrieved AppUsageControls object.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `app_usage_controls`                                                            | [Optional[AppUsageControls]](../../models/shared/appusagecontrols.md)           | :heavy_minus_sign:                                                              | The AppUsageControls object describes some peripheral configuration for an app. |
| `has_usage_data`                                                                | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | HasUsageData is false if the access entitlement for this app has no usage data. |