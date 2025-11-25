# AutomationExecutionSearch
(*automation_execution_search*)

## Overview

### Available Operations

* [search_automation_executions](#search_automation_executions) - Search Automation Executions

## search_automation_executions

Invokes the c1.api.automations.v1.AutomationExecutionSearchService.SearchAutomationExecutions method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationExecutionSearchService.SearchAutomationExecutions" method="post" path="/api/v1/automation_executions/search" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation_execution_search.search_automation_executions()

    assert res.search_automation_executions_response is not None

    # Handle response
    print(res.search_automation_executions_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SearchAutomationExecutionsRequest](../../models/shared/searchautomationexecutionsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.C1APIAutomationsV1AutomationExecutionSearchServiceSearchAutomationExecutionsResponse](../../models/operations/c1apiautomationsv1automationexecutionsearchservicesearchautomationexecutionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |