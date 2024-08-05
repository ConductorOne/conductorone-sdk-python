# ExportsSearchServiceSearchRequest

The ExportsSearchServiceSearchRequest message.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `display_name`                                                                     | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Search for system log exporters with a case insensitive match on the display name. |
| `page_size`                                                                        | *Optional[int]*                                                                    | :heavy_minus_sign:                                                                 | The pageSize field.                                                                |
| `page_token`                                                                       | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The pageToken field.                                                               |
| `query`                                                                            | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | The query field.                                                                   |
| `refs`                                                                             | List[[shared.ExporterRef](../../models/shared/exporterref.md)]                     | :heavy_minus_sign:                                                                 | The refs field.                                                                    |