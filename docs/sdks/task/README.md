# Task
(*task*)

## Overview

### Available Operations

* [create_grant_task](#create_grant_task) - Create Grant Task
* [create_offboarding_task](#create_offboarding_task) - Create Offboarding Task
* [create_revoke_task](#create_revoke_task) - Create Revoke Task
* [get](#get) - Get

## create_grant_task

Create a grant task

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskService.CreateGrantTask" method="post" path="/api/v1/task/grant" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.task.create_grant_task(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.task_service_create_grant_response is not None

    # Handle response
    print(res.task_service_create_grant_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.TaskServiceCreateGrantRequest](../../models/shared/taskservicecreategrantrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.C1APITaskV1TaskServiceCreateGrantTaskResponse](../../models/operations/c1apitaskv1taskservicecreategranttaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_offboarding_task

Invokes the c1.api.task.v1.TaskService.CreateOffboardingTask method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskService.CreateOffboardingTask" method="post" path="/api/v1/task/offboarding" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.task.create_offboarding_task(request={})

    assert res.task_service_create_offboarding_response is not None

    # Handle response
    print(res.task_service_create_offboarding_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.TaskServiceCreateOffboardingRequest](../../models/shared/taskservicecreateoffboardingrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.C1APITaskV1TaskServiceCreateOffboardingTaskResponse](../../models/operations/c1apitaskv1taskservicecreateoffboardingtaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_revoke_task

Create a revoke task

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskService.CreateRevokeTask" method="post" path="/api/v1/task/revoke" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.task.create_revoke_task(request={
        "app_entitlement_id": "<id>",
        "app_id": "<id>",
    })

    assert res.task_service_create_revoke_response is not None

    # Handle response
    print(res.task_service_create_revoke_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [shared.TaskServiceCreateRevokeRequest](../../models/shared/taskservicecreaterevokerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.C1APITaskV1TaskServiceCreateRevokeTaskResponse](../../models/operations/c1apitaskv1taskservicecreaterevoketaskresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Get a task by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskService.Get" method="get" path="/api/v1/tasks/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.task.get(request={
        "id": "<id>",
    })

    assert res.task_service_get_response is not None

    # Handle response
    print(res.task_service_get_response)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.C1APITaskV1TaskServiceGetRequest](../../models/operations/c1apitaskv1taskservicegetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.C1APITaskV1TaskServiceGetResponse](../../models/operations/c1apitaskv1taskservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |