# AppResourceServiceUpdateRequest

The AppResourceServiceUpdateRequest message.


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `app_resource`                                                                                | [Optional[shared.AppResourceInput]](../../models/shared/appresourceinput.md)                  | :heavy_minus_sign:                                                                            | The app resource message is a single resource that can have entitlements.                     |
| `app_resource_expand_mask`                                                                    | [Optional[shared.AppResourceExpandMask]](../../models/shared/appresourceexpandmask.md)        | :heavy_minus_sign:                                                                            | The app resource expand mask lets you get information about related objects from the request. |
| `update_mask`                                                                                 | *OptionalNullable[str]*                                                                       | :heavy_minus_sign:                                                                            | N/A                                                                                           |