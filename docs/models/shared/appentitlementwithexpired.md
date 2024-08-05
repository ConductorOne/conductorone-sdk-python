# AppEntitlementWithExpired

The AppEntitlementWithExpired message.


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `app_user`                                                                              | [Optional[shared.AppUser]](../../models/shared/appuser.md)                              | :heavy_minus_sign:                                                                      | Application User that represents an account in the application.                         |
| `user`                                                                                  | [Optional[shared.User]](../../models/shared/user.md)                                    | :heavy_minus_sign:                                                                      | The User object provides all of the details for an user, as well as some configuration. |
| `discovered`                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `expired`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_minus_sign:                                                                      | N/A                                                                                     |