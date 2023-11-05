# PersonalClientServiceCreateRequest

The PersonalClientServiceCreateRequest message contains the fields for creating a new personal client.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `allow_source_cidr`                              | List[*str*]                                      | :heavy_minus_sign:                               | A list of CIDRs to restrict this credential to.  |
| `display_name`                                   | *Optional[str]*                                  | :heavy_minus_sign:                               | The display name for the new personal client.    |
| `expires`                                        | *Optional[str]*                                  | :heavy_minus_sign:                               | N/A                                              |
| `scoped_roles`                                   | List[*str*]                                      | :heavy_minus_sign:                               | The list of roles to restrict the credential to. |