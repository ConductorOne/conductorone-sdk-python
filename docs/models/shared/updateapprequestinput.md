# UpdateAppRequestInput

The UpdateAppRequest message contains the app to update and the fields to update.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `app`                                                                                 | [Optional[shared.AppInput]](undefined/models/shared/appinput.md)                      | :heavy_minus_sign:                                                                    | The App object provides all of the details for an app, as well as some configuration. |
| `update_mask`                                                                         | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | N/A                                                                                   |