# TaskActions
(*task_actions*)

## Overview

### Available Operations

* [approve](#approve) - Approve
* [approve_with_step_up](#approve_with_step_up) - Approve With Step Up
* [close](#close) - Close
* [comment](#comment) - Comment
* [deny](#deny) - Deny
* [escalate_to_emergency_access](#escalate_to_emergency_access) - Escalate To Emergency Access
* [hard_reset](#hard_reset) - Hard Reset
* [process_now](#process_now) - Process Now
* [reassign](#reassign) - Reassign
* [restart](#restart) - Restart
* [skip_step](#skip_step) - Skip Step
* [update_grant_duration](#update_grant_duration) - Update Grant Duration
* [update_request_data](#update_request_data) - Update Request Data

## approve

Invokes the c1.api.task.v1.TaskActionsService.Approve method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.Approve" method="post" path="/api/v1/tasks/{task_id}/action/approve" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.approve(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_approve_response is not None

    # Handle response
    print(res.task_actions_service_approve_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceApproveRequest](../../models/operations/c1apitaskv1taskactionsserviceapproverequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APITaskV1TaskActionsServiceApproveResponse](../../models/operations/c1apitaskv1taskactionsserviceapproveresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## approve_with_step_up

Invokes the c1.api.task.v1.TaskActionsService.ApproveWithStepUp method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.ApproveWithStepUp" method="post" path="/api/v1/tasks/{task_id}/action/approve-with-step-up" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.approve_with_step_up(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_approve_with_step_up_response is not None

    # Handle response
    print(res.task_actions_service_approve_with_step_up_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APITaskV1TaskActionsServiceApproveWithStepUpRequest](../../models/operations/c1apitaskv1taskactionsserviceapprovewithstepuprequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APITaskV1TaskActionsServiceApproveWithStepUpResponse](../../models/operations/c1apitaskv1taskactionsserviceapprovewithstepupresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## close

Invokes the c1.api.task.v1.TaskActionsService.Close method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.Close" method="post" path="/api/v1/tasks/{task_id}/action/close" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.close(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_close_response is not None

    # Handle response
    print(res.task_actions_service_close_response)

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APITaskV1TaskActionsServiceCloseRequest](../../models/operations/c1apitaskv1taskactionsservicecloserequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |
| `retries`                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                             | :heavy_minus_sign:                                                                                                           | Configuration to override the default retry behavior of the client.                                                          |

### Response

**[operations.C1APITaskV1TaskActionsServiceCloseResponse](../../models/operations/c1apitaskv1taskactionsservicecloseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## comment

Invokes the c1.api.task.v1.TaskActionsService.Comment method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.Comment" method="post" path="/api/v1/tasks/{task_id}/action/comment" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.comment(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_comment_response is not None

    # Handle response
    print(res.task_actions_service_comment_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceCommentRequest](../../models/operations/c1apitaskv1taskactionsservicecommentrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APITaskV1TaskActionsServiceCommentResponse](../../models/operations/c1apitaskv1taskactionsservicecommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## deny

Invokes the c1.api.task.v1.TaskActionsService.Deny method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.Deny" method="post" path="/api/v1/tasks/{task_id}/action/deny" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.deny(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_deny_response is not None

    # Handle response
    print(res.task_actions_service_deny_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APITaskV1TaskActionsServiceDenyRequest](../../models/operations/c1apitaskv1taskactionsservicedenyrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APITaskV1TaskActionsServiceDenyResponse](../../models/operations/c1apitaskv1taskactionsservicedenyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## escalate_to_emergency_access

Invokes the c1.api.task.v1.TaskActionsService.EscalateToEmergencyAccess method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.EscalateToEmergencyAccess" method="post" path="/api/v1/tasks/{task_id}/action/escalate" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.escalate_to_emergency_access(request={
        "task_id": "<id>",
    })

    assert res.task_service_action_response is not None

    # Handle response
    print(res.task_service_action_response)

```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessRequest](../../models/operations/c1apitaskv1taskactionsserviceescalatetoemergencyaccessrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |
| `retries`                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                     | :heavy_minus_sign:                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                  |

### Response

**[operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessResponse](../../models/operations/c1apitaskv1taskactionsserviceescalatetoemergencyaccessresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## hard_reset

Invokes the c1.api.task.v1.TaskActionsService.HardReset method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.HardReset" method="post" path="/api/v1/tasks/{task_id}/action/reset" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.hard_reset(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_hard_reset_response is not None

    # Handle response
    print(res.task_actions_service_hard_reset_response)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.C1APITaskV1TaskActionsServiceHardResetRequest](../../models/operations/c1apitaskv1taskactionsservicehardresetrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.C1APITaskV1TaskActionsServiceHardResetResponse](../../models/operations/c1apitaskv1taskactionsservicehardresetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## process_now

Invokes the c1.api.task.v1.TaskActionsService.ProcessNow method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.ProcessNow" method="post" path="/api/v1/tasks/{task_id}/action/process" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.process_now(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_process_now_response is not None

    # Handle response
    print(res.task_actions_service_process_now_response)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.C1APITaskV1TaskActionsServiceProcessNowRequest](../../models/operations/c1apitaskv1taskactionsserviceprocessnowrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[operations.C1APITaskV1TaskActionsServiceProcessNowResponse](../../models/operations/c1apitaskv1taskactionsserviceprocessnowresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## reassign

Invokes the c1.api.task.v1.TaskActionsService.Reassign method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.Reassign" method="post" path="/api/v1/tasks/{task_id}/action/reassign" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.reassign(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_reassign_response is not None

    # Handle response
    print(res.task_actions_service_reassign_response)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.C1APITaskV1TaskActionsServiceReassignRequest](../../models/operations/c1apitaskv1taskactionsservicereassignrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[operations.C1APITaskV1TaskActionsServiceReassignResponse](../../models/operations/c1apitaskv1taskactionsservicereassignresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## restart

Invokes the c1.api.task.v1.TaskActionsService.Restart method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.Restart" method="post" path="/api/v1/tasks/{task_id}/action/restart" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.restart(request={
        "task_id": "<id>",
    })

    assert res.task_actions_service_restart_response is not None

    # Handle response
    print(res.task_actions_service_restart_response)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceRestartRequest](../../models/operations/c1apitaskv1taskactionsservicerestartrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[operations.C1APITaskV1TaskActionsServiceRestartResponse](../../models/operations/c1apitaskv1taskactionsservicerestartresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## skip_step

Invokes the c1.api.task.v1.TaskActionsService.SkipStep method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.SkipStep" method="post" path="/api/v1/tasks/{task_id}/action/skip-step" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.skip_step(request={
        "task_id": "<id>",
    })

    assert res.task_service_action_response is not None

    # Handle response
    print(res.task_service_action_response)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.C1APITaskV1TaskActionsServiceSkipStepRequest](../../models/operations/c1apitaskv1taskactionsserviceskipsteprequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[operations.C1APITaskV1TaskActionsServiceSkipStepResponse](../../models/operations/c1apitaskv1taskactionsserviceskipstepresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_grant_duration

Invokes the c1.api.task.v1.TaskActionsService.UpdateGrantDuration method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.UpdateGrantDuration" method="post" path="/api/v1/tasks/{task_id}/action/update-grant-duration" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.update_grant_duration(request={
        "task_id": "<id>",
    })

    assert res.task_service_action_response is not None

    # Handle response
    print(res.task_service_action_response)

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.C1APITaskV1TaskActionsServiceUpdateGrantDurationRequest](../../models/operations/c1apitaskv1taskactionsserviceupdategrantdurationrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |
| `retries`                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                         | :heavy_minus_sign:                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                      |

### Response

**[operations.C1APITaskV1TaskActionsServiceUpdateGrantDurationResponse](../../models/operations/c1apitaskv1taskactionsserviceupdategrantdurationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_request_data

Invokes the c1.api.task.v1.TaskActionsService.UpdateRequestData method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskActionsService.UpdateRequestData" method="post" path="/api/v1/tasks/{task_id}/action/update-request-data" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.task_actions.update_request_data(request={
        "task_id": "<id>",
    })

    assert res.task_service_action_response is not None

    # Handle response
    print(res.task_service_action_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APITaskV1TaskActionsServiceUpdateRequestDataRequest](../../models/operations/c1apitaskv1taskactionsserviceupdaterequestdatarequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APITaskV1TaskActionsServiceUpdateRequestDataResponse](../../models/operations/c1apitaskv1taskactionsserviceupdaterequestdataresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |