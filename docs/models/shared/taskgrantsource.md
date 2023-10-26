# TaskGrantSource

The TaskGrantSource message tracks which external URL was the source of the specificed grant ticket.


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `external_url`                                | *Optional[str]*                               | :heavy_minus_sign:                            | The external url source of the grant ticket.  |
| `integration_id`                              | *Optional[str]*                               | :heavy_minus_sign:                            | The integration id for the source of tickets. |