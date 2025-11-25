# Vault

The Vault message.

This message contains a oneof named vault. Only a single field of the following list may be set at a time:
  - groupAuthzVault
  - magicVault



## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `group_authz_vault`                                                                | [OptionalNullable[shared.GroupAuthzVault]](../../models/shared/groupauthzvault.md) | :heavy_minus_sign:                                                                 | The GroupAuthzVault message.                                                       |
| `magic_vault`                                                                      | [OptionalNullable[shared.MagicVault]](../../models/shared/magicvault.md)           | :heavy_minus_sign:                                                                 | The MagicVault message.                                                            |
| `created_at`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `credential_expiration_duration`                                                   | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `deleted_at`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `description`                                                                      | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The description field.                                                             |
| `display_name`                                                                     | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The displayName field.                                                             |
| `id`                                                                               | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The id field.                                                                      |
| `updated_at`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_minus_sign:                                                                 | N/A                                                                                |