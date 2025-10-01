# UnenrollFromAllAccessProfiles

The UnenrollFromAllAccessProfiles message.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `catalog_ids`                                                                         | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | Optional list of catalog IDs to unenroll from. If empty, unenroll from all catalogs.  |
| `catalog_ids_cel`                                                                     | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | CEL expression to dynamically select catalog IDs. If provided, overrides catalog_ids. |
| `use_subject_user`                                                                    | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | If true, the step will use the subject user of the automation as the subject.         |
| `user_ids_cel`                                                                        | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | The userIdsCel field.                                                                 |
| `user_refs`                                                                           | List[[shared.UserRef](../../models/shared/userref.md)]                                | :heavy_minus_sign:                                                                    | The userRefs field.                                                                   |