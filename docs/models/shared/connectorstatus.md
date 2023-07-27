# ConnectorStatus

The status field on the connector is used to track the status of the connectors sync, and when syncing last started, completed, or caused the connector to update.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `completed_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)            | :heavy_minus_sign:                                                              | N/A                                                                             |
| `last_error`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The last error encountered by the connector.                                    |
| `started_at`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)            | :heavy_minus_sign:                                                              | N/A                                                                             |
| `status`                                                                        | [Optional[ConnectorStatusStatus]](../../models/shared/connectorstatusstatus.md) | :heavy_minus_sign:                                                              | The status of the connector sync.                                               |
| `updated_at`                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)            | :heavy_minus_sign:                                                              | N/A                                                                             |