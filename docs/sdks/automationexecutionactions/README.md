# AutomationExecutionActions
(*automation_execution_actions*)

## Overview

### Available Operations

* [terminate_automation](#terminate_automation) - Terminate Automation

## terminate_automation

Invokes the c1.api.automations.v1.AutomationExecutionActionsService.TerminateAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationExecutionActionsService.TerminateAutomation" method="post" path="/api/v1/automation_executions/{id}/actions/terminate" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation_execution_actions.terminate_automation(request={
        "id": 839265,
    })

    assert res.terminate_automation_response is not None

    # Handle response
    print(res.terminate_automation_response)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                            | [operations.C1APIAutomationsV1AutomationExecutionActionsServiceTerminateAutomationRequest](../../models/operations/c1apiautomationsv1automationexecutionactionsserviceterminateautomationrequest.md) | :heavy_check_mark:                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                           |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |

### Response

**[operations.C1APIAutomationsV1AutomationExecutionActionsServiceTerminateAutomationResponse](../../models/operations/c1apiautomationsv1automationexecutionactionsserviceterminateautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |