# PersonalClientSearchServiceSearchRequest

The PersonalClientSearchServiceSearchRequest message.


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `page_size`                                            | *Optional[int]*                                        | :heavy_minus_sign:                                     | The pageSize field.                                    |
| `page_token`                                           | *Optional[str]*                                        | :heavy_minus_sign:                                     | The pageToken field.                                   |
| `query`                                                | *Optional[str]*                                        | :heavy_minus_sign:                                     | The query field.                                       |
| `users`                                                | List[[shared.UserRef](../../models/shared/userref.md)] | :heavy_minus_sign:                                     | The users field.                                       |