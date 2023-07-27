# app_report

### Available Operations

* [list](#list) - List

## list

Get a list of reports for the given app.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppReportServiceListRequest(
    app_id='aliquid',
    page_size=5865.13,
    page_token='quos',
)

res = s.app_report.list(req)

if res.app_report_service_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1AppReportServiceListRequest](../../models/operations/c1apiappv1appreportservicelistrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.C1APIAppV1AppReportServiceListResponse](../../models/operations/c1apiappv1appreportservicelistresponse.md)**

