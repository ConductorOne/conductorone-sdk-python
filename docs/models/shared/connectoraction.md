# ConnectorAction

The ConnectorAction message.

This message contains a oneof named connector_identifier. Only a single field of the following list may be set at a time:
  - connectorRef



## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `connector_ref`                                                              | [OptionalNullable[shared.ConnectorRef]](../../models/shared/connectorref.md) | :heavy_minus_sign:                                                           | The ConnectorRef message.                                                    |
| `action_name`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The actionName field.                                                        |
| `args_template`                                                              | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |