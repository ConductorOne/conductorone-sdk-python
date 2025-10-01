# SendEmail

The SendEmail message.


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `body`                                                                        | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The body field.                                                               |
| `subject`                                                                     | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The subject field.                                                            |
| `title`                                                                       | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The title field.                                                              |
| `use_subject_user`                                                            | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | If true, the step will use the subject user of the automation as the subject. |
| `user_ids_cel`                                                                | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The userIdsCel field.                                                         |
| `user_refs`                                                                   | List[[shared.UserRef](../../models/shared/userref.md)]                        | :heavy_minus_sign:                                                            | The userRefs field.                                                           |