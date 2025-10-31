# AccountProvision

The AccountProvision message.

This message contains a oneof named storage_type. Only a single field of the following list may be set at a time:
  - saveToVault
  - doNotSave



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `do_not_save`                                                              | [OptionalNullable[shared.DoNotSave]](../../models/shared/donotsave.md)     | :heavy_minus_sign:                                                         | The DoNotSave message.                                                     |
| `save_to_vault`                                                            | [OptionalNullable[shared.SaveToVault]](../../models/shared/savetovault.md) | :heavy_minus_sign:                                                         | The SaveToVault message.                                                   |
| `config`                                                                   | Dict[str, *Any*]                                                           | :heavy_minus_sign:                                                         | N/A                                                                        |
| `connector_id`                                                             | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The connectorId field.                                                     |
| `schema_id`                                                                | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The schemaId field.                                                        |