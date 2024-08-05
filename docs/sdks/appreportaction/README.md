# AppReportAction
(*app_report_action*)

### Available Operations

* [generate_report](#generate_report) - Generate Report

## generate_report

Generate a report for the given app.

### Example Usage

```python
from sdk import SDK
from sdk.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_report_action.generate_report(request={
    "app_id": "<value>",
})

if res.app_actions_service_generate_report_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIAppV1AppReportActionServiceGenerateReportRequest](../../models/operations/c1apiappv1appreportactionservicegeneratereportrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |


### Response

**[operations.C1APIAppV1AppReportActionServiceGenerateReportResponse](../../models/operations/c1apiappv1appreportactionservicegeneratereportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
