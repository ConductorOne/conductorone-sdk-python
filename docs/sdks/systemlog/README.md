# SystemLog
(*system_log*)

## Overview

### Available Operations

* [list_events](#list_events) - List Events

## list_events

ListEvents pulls Events from the ConductorOne system.

 This endpoint should be used to synchorize the
 system log events to external systems.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.systemlog.v1.SystemLogService.ListEvents" method="post" path="/api/v1/systemlog/events" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.system_log.list_events()

    assert res.system_log_service_list_events_response is not None

    # Handle response
    print(res.system_log_service_list_events_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SystemLogServiceListEventsRequest](../../models/shared/systemlogservicelisteventsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.C1APISystemlogV1SystemLogServiceListEventsResponse](../../models/operations/c1apisystemlogv1systemlogservicelisteventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |