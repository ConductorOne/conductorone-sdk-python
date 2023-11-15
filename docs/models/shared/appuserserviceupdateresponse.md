# AppUserServiceUpdateResponse

The AppUserServiceUpdateResponse message.


## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `app_user_view`                                                                                                    | [Optional[shared.AppUserView]](../../models/shared/appuserview.md)                                                 | :heavy_minus_sign:                                                                                                 | The AppUserView contains an app user as well as paths for apps, identity users, and last usage in expanded arrays. |
| `expanded`                                                                                                         | List[[shared.AppUserServiceUpdateResponseExpanded](../../models/shared/appuserserviceupdateresponseexpanded.md)]   | :heavy_minus_sign:                                                                                                 | The expanded field.                                                                                                |