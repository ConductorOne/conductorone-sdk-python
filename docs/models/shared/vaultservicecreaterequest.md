# VaultServiceCreateRequest

The VaultServiceCreateRequest message.

This message contains a oneof named vault. Only a single field of the following list may be set at a time:
  - groupAuthzVault
  - magicVault



## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `group_authz_vault`                                                                | [OptionalNullable[shared.GroupAuthzVault]](../../models/shared/groupauthzvault.md) | :heavy_minus_sign:                                                                 | The GroupAuthzVault message.                                                       |
| `magic_vault`                                                                      | [OptionalNullable[shared.MagicVault]](../../models/shared/magicvault.md)           | :heavy_minus_sign:                                                                 | The MagicVault message.                                                            |
| `description`                                                                      | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The description field.                                                             |
| `display_name`                                                                     | *str*                                                                              | :heavy_check_mark:                                                                 | The displayName field.                                                             |
| `owner_ids`                                                                        | List[*str*]                                                                        | :heavy_minus_sign:                                                                 | The ownerIds field.                                                                |