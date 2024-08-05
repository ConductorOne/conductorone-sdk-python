# C1APISystemlogV1SystemLogServiceListEventsResponse


## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                   | *str*                                                                                                            | :heavy_check_mark:                                                                                               | HTTP response content type for this operation                                                                    |
| `status_code`                                                                                                    | *int*                                                                                                            | :heavy_check_mark:                                                                                               | HTTP response status code for this operation                                                                     |
| `raw_response`                                                                                                   | [httpx.Response](https://www.python-httpx.org/api/#response)                                                     | :heavy_check_mark:                                                                                               | Raw HTTP response; suitable for custom response parsing                                                          |
| `system_log_service_list_events_response`                                                                        | [Optional[shared.SystemLogServiceListEventsResponse]](../../models/shared/systemlogservicelisteventsresponse.md) | :heavy_minus_sign:                                                                                               | Successful response                                                                                              |