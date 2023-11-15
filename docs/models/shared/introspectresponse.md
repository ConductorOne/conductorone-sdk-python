# IntrospectResponse

IntrospectResponse contains information about the current user who is authenticated.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `features`                                                                      | List[*str*]                                                                     | :heavy_minus_sign:                                                              | The list of feature flags enabled for the tenant the logged in user belongs to. |
| `permissions`                                                                   | List[*str*]                                                                     | :heavy_minus_sign:                                                              | The list of permissions that the current logged in user has.                    |
| `principle_id`                                                                  | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The principleID of the current logged in user.                                  |
| `roles`                                                                         | List[*str*]                                                                     | :heavy_minus_sign:                                                              | The list of roles that the current logged in user has.                          |
| `user_id`                                                                       | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The userID of the current logged in user.                                       |