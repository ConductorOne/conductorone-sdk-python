# AutomationExecution
(*automation_execution*)

## Overview

### Available Operations

* [get_automation_execution](#get_automation_execution) - Get Automation Execution
* [list_automation_executions](#list_automation_executions) - List Automation Executions

## get_automation_execution

Invokes the c1.api.automations.v1.AutomationExecutionService.GetAutomationExecution method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationExecutionService.GetAutomationExecution" method="get" path="/api/v1/automation_executions/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation_execution.get_automation_execution(request={
        "id": 728203,
    })

    assert res.get_automation_execution_response is not None

    # Handle response
    print(res.get_automation_execution_response)

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                    | [operations.C1APIAutomationsV1AutomationExecutionServiceGetAutomationExecutionRequest](../../models/operations/c1apiautomationsv1automationexecutionservicegetautomationexecutionrequest.md) | :heavy_check_mark:                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                   |
| `retries`                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                          |

### Response

**[operations.C1APIAutomationsV1AutomationExecutionServiceGetAutomationExecutionResponse](../../models/operations/c1apiautomationsv1automationexecutionservicegetautomationexecutionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_automation_executions

Invokes the c1.api.automations.v1.AutomationExecutionService.ListAutomationExecutions method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationExecutionService.ListAutomationExecutions" method="get" path="/api/v1/automation_executions" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation_execution.list_automation_executions()

    assert res.list_automation_executions_response is not None

    # Handle response
    print(res.list_automation_executions_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APIAutomationsV1AutomationExecutionServiceListAutomationExecutionsResponse](../../models/operations/c1apiautomationsv1automationexecutionservicelistautomationexecutionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |