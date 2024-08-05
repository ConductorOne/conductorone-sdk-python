# AppUserServiceUpdateRequest

The AppUserServiceUpdateRequest message contains the app user and the fields to be updated.


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `app_user`                                                                        | [Optional[shared.AppUserInput]](../../models/shared/appuserinput.md)              | :heavy_minus_sign:                                                                | Application User that represents an account in the application.                   |
| `app_user_expand_mask`                                                            | [Optional[shared.AppUserExpandMask]](../../models/shared/appuserexpandmask.md)    | :heavy_minus_sign:                                                                | The AppUserExpandMask message contains a list of paths to expand in the response. |
| `update_mask`                                                                     | *OptionalNullable[str]*                                                           | :heavy_minus_sign:                                                                | N/A                                                                               |