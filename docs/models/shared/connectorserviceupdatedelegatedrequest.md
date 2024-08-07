# ConnectorServiceUpdateDelegatedRequest

The ConnectorServiceUpdateDelegatedRequest message contains the fields required to update a connector.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `connector`                                                                        | [Optional[shared.ConnectorInput]](../../models/shared/connectorinput.md)           | :heavy_minus_sign:                                                                 | A Connector is used to sync objects into Apps                                      |
| `connector_expand_mask`                                                            | [Optional[shared.ConnectorExpandMask]](../../models/shared/connectorexpandmask.md) | :heavy_minus_sign:                                                                 | The ConnectorExpandMask is used to expand related objects on a connector.          |
| `update_mask`                                                                      | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | N/A                                                                                |