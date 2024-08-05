# SystemLogServiceListEventsRequest

The SystemLogServiceListEventsRequest message.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `page_size`                                                            | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | The pageSize field.                                                    |
| `page_token`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The pageToken field.                                                   |
| `since`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | N/A                                                                    |
| `since_event_uid`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | The sinceEventUid field.                                               |
| `sort_direction`                                                       | [Optional[shared.SortDirection]](../../models/shared/sortdirection.md) | :heavy_minus_sign:                                                     | The sortDirection field.                                               |
| `until`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | N/A                                                                    |