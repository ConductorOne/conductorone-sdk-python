# AccountLifecycleAction

The AccountLifecycleAction message.

This message contains a oneof named account_identifier. Only a single field of the following list may be set at a time:
  - accountRef
  - accountInContext



## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `account_in_context`                                                                 | [OptionalNullable[shared.AccountInContext]](../../models/shared/accountincontext.md) | :heavy_minus_sign:                                                                   | The AccountInContext message.                                                        |
| `account_ref`                                                                        | [OptionalNullable[shared.AccountRef]](../../models/shared/accountref.md)             | :heavy_minus_sign:                                                                   | The AccountRef message.                                                              |
| `connector_ref`                                                                      | [OptionalNullable[shared.ConnectorRef]](../../models/shared/connectorref.md)         | :heavy_minus_sign:                                                                   | The ConnectorRef message.                                                            |
| `action_name`                                                                        | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | The actionName field.                                                                |