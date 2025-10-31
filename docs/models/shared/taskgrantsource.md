# TaskGrantSource

The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `conversation_id`                                             | *Optional[str]*                                               | :heavy_minus_sign:                                            | The ID of the conversation that created this ticket           |
| `external_url`                                                | *Optional[str]*                                               | :heavy_minus_sign:                                            | The external url source of the grant ticket.                  |
| `integration_id`                                              | *Optional[str]*                                               | :heavy_minus_sign:                                            | The integration id for the source of tickets.                 |
| `request_id`                                                  | *Optional[str]*                                               | :heavy_minus_sign:                                            | the request id for the grant ticket if the source is external |