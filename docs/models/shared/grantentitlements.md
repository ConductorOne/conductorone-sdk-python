# GrantEntitlements

The GrantEntitlements message.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `user_ref`                                                                    | [Optional[shared.UserRef]](../../models/shared/userref.md)                    | :heavy_minus_sign:                                                            | A reference to a user.                                                        |
| `app_entitlement_refs`                                                        | List[[shared.AppEntitlementRef](../../models/shared/appentitlementref.md)]    | :heavy_minus_sign:                                                            | The appEntitlementRefs field.                                                 |
| `app_entitlement_refs_cel`                                                    | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The appEntitlementRefsCel field.                                              |
| `use_subject_user`                                                            | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | If true, the step will use the subject user of the automation as the subject. |
| `user_id_cel`                                                                 | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The userIdCel field.                                                          |