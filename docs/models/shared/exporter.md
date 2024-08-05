# Exporter

The Exporter message.

This message contains a oneof named export_to. Only a single field of the following list may be set at a time:
  - datasource



## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `export_to_datasource`                                                                   | [OptionalNullable[shared.ExportToDatasource]](../../models/shared/exporttodatasource.md) | :heavy_minus_sign:                                                                       | The ExportToDatasource message.                                                          |
| `created_at`                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                     | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `deleted_at`                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                     | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `display_name`                                                                           | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | The displayName field.                                                                   |
| `export_id`                                                                              | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | The exportId field.                                                                      |
| `state`                                                                                  | [Optional[shared.ExporterState]](../../models/shared/exporterstate.md)                   | :heavy_minus_sign:                                                                       | The state field.                                                                         |
| `updated_at`                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                     | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `watermark_event_id`                                                                     | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | we've synchorized this far                                                               |