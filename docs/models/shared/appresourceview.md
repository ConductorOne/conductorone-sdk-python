# AppResourceView

The app resource view returns an app resource with paths for items in the expand mask filled in when this response is returned and a request expand mask has "*" or "app_id" or "resource_type_id".


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `app_resource`                                                                       | [Optional[AppResource]](../../models/shared/appresource.md)                          | :heavy_minus_sign:                                                                   | The app resource message is a single resource that can have entitlements.            |
| `app_path`                                                                           | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | JSONPATH expression indicating the location of the App object in the array           |
| `resource_type_path`                                                                 | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | JSONPATH expression indicating the location of the Resource Type object in the array |