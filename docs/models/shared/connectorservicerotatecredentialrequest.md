# ConnectorServiceRotateCredentialRequest

ConnectorServiceRotateCredentialRequest is a request for rotating connector credentials. It uses URL values for input.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `app_id`                                                                   | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The appId of the app the connector is attached to.                         |
| `connector_id`                                                             | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The connectorId of the connector that we are rotating the credentials for. |