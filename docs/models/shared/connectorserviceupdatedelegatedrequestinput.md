# ConnectorServiceUpdateDelegatedRequestInput

The ConnectorServiceUpdateDelegatedRequest message contains the fields required to update a connector.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `connector`                                                                            | [Optional[shared.ConnectorInput]](undefined/models/shared/connectorinput.md)           | :heavy_minus_sign:                                                                     | A Connector is used to sync objects into Apps                                          |
| `connector_expand_mask`                                                                | [Optional[shared.ConnectorExpandMask]](undefined/models/shared/connectorexpandmask.md) | :heavy_minus_sign:                                                                     | The ConnectorExpandMask is used to expand related objects on a connector.              |
| `update_mask`                                                                          | *Optional[str]*                                                                        | :heavy_minus_sign:                                                                     | N/A                                                                                    |