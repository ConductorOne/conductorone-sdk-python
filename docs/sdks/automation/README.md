# Automation
(*automation*)

## Overview

### Available Operations

* [create_automation](#create_automation) - Create Automation
* [delete_automation](#delete_automation) - Delete Automation
* [execute_automation](#execute_automation) - Execute Automation
* [get_automation](#get_automation) - Get Automation
* [list_automations](#list_automations) - List Automations
* [update_automation](#update_automation) - Update Automation

## create_automation

Invokes the c1.api.automations.v1.AutomationService.CreateAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationService.CreateAutomation" method="post" path="/api/v1/automations" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation.create_automation()

    assert res.create_automation_response is not None

    # Handle response
    print(res.create_automation_response)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.CreateAutomationRequestInput](../../models/shared/createautomationrequestinput.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.C1APIAutomationsV1AutomationServiceCreateAutomationResponse](../../models/operations/c1apiautomationsv1automationservicecreateautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_automation

Invokes the c1.api.automations.v1.AutomationService.DeleteAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationService.DeleteAutomation" method="delete" path="/api/v1/automations/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation.delete_automation(request={
        "id": "<id>",
    })

    assert res.delete_automation_response is not None

    # Handle response
    print(res.delete_automation_response)

```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.C1APIAutomationsV1AutomationServiceDeleteAutomationRequest](../../models/operations/c1apiautomationsv1automationservicedeleteautomationrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |
| `retries`                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                               | :heavy_minus_sign:                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                            |

### Response

**[operations.C1APIAutomationsV1AutomationServiceDeleteAutomationResponse](../../models/operations/c1apiautomationsv1automationservicedeleteautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## execute_automation

Invokes the c1.api.automations.v1.AutomationService.ExecuteAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationService.ExecuteAutomation" method="post" path="/api/v1/automations/{id}/execute" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation.execute_automation(request={
        "id": "<id>",
    })

    assert res.execute_automation_response is not None

    # Handle response
    print(res.execute_automation_response)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.C1APIAutomationsV1AutomationServiceExecuteAutomationRequest](../../models/operations/c1apiautomationsv1automationserviceexecuteautomationrequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |

### Response

**[operations.C1APIAutomationsV1AutomationServiceExecuteAutomationResponse](../../models/operations/c1apiautomationsv1automationserviceexecuteautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_automation

Invokes the c1.api.automations.v1.AutomationService.GetAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationService.GetAutomation" method="get" path="/api/v1/automations/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation.get_automation(request={
        "id": "<id>",
    })

    assert res.get_automation_response is not None

    # Handle response
    print(res.get_automation_response)

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.C1APIAutomationsV1AutomationServiceGetAutomationRequest](../../models/operations/c1apiautomationsv1automationservicegetautomationrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |
| `retries`                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                         | :heavy_minus_sign:                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                      |

### Response

**[operations.C1APIAutomationsV1AutomationServiceGetAutomationResponse](../../models/operations/c1apiautomationsv1automationservicegetautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_automations

Invokes the c1.api.automations.v1.AutomationService.ListAutomations method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationService.ListAutomations" method="get" path="/api/v1/automations" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation.list_automations()

    assert res.list_automations_response is not None

    # Handle response
    print(res.list_automations_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.C1APIAutomationsV1AutomationServiceListAutomationsResponse](../../models/operations/c1apiautomationsv1automationservicelistautomationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_automation

Invokes the c1.api.automations.v1.AutomationService.UpdateAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationService.UpdateAutomation" method="post" path="/api/v1/automations/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.automation.update_automation(request={
        "id": "<id>",
    })

    assert res.update_automation_response is not None

    # Handle response
    print(res.update_automation_response)

```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.C1APIAutomationsV1AutomationServiceUpdateAutomationRequest](../../models/operations/c1apiautomationsv1automationserviceupdateautomationrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |
| `retries`                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                               | :heavy_minus_sign:                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                            |

### Response

**[operations.C1APIAutomationsV1AutomationServiceUpdateAutomationResponse](../../models/operations/c1apiautomationsv1automationserviceupdateautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |