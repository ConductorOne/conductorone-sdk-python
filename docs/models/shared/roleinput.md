# RoleInput

Role is a role that can be assigned to a user in ConductorOne.


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `display_name`                               | *Optional[str]*                              | :heavy_minus_sign:                           | The display name of the role.                |
| `permissions`                                | List[*str*]                                  | :heavy_minus_sign:                           | The list of permissions this role has.       |
| `service_roles`                              | List[*str*]                                  | :heavy_minus_sign:                           | The list of serviceRoles that this role has. |