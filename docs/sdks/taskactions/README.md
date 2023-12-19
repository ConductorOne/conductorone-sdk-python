# TaskActions
(*task_actions*)

### Available Operations

* [approve](#approve) - Approve
* [comment](#comment) - Comment
* [deny](#deny) - Deny
* [escalate_to_emergency_access](#escalate_to_emergency_access) - Escalate To Emergency Access
* [restart](#restart) - Restart

## approve

Invokes the c1.api.task.v1.TaskActionsService.Approve method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceApproveRequest(
    task_actions_service_approve_request=shared.TaskActionsServiceApproveRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'string',
            ],
        ),
        policy_step_id='string',
    ),
    task_id='string',
)

res = s.task_actions.approve(req)

if res.task_actions_service_approve_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceApproveRequest](../../models/operations/c1apitaskv1taskactionsserviceapproverequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APITaskV1TaskActionsServiceApproveResponse](../../models/operations/c1apitaskv1taskactionsserviceapproveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## comment

Invokes the c1.api.task.v1.TaskActionsService.Comment method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceCommentRequest(
    task_actions_service_comment_request=shared.TaskActionsServiceCommentRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'string',
            ],
        ),
    ),
    task_id='string',
)

res = s.task_actions.comment(req)

if res.task_actions_service_comment_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceCommentRequest](../../models/operations/c1apitaskv1taskactionsservicecommentrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APITaskV1TaskActionsServiceCommentResponse](../../models/operations/c1apitaskv1taskactionsservicecommentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## deny

Invokes the c1.api.task.v1.TaskActionsService.Deny method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceDenyRequest(
    task_actions_service_deny_request=shared.TaskActionsServiceDenyRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'string',
            ],
        ),
    ),
    task_id='string',
)

res = s.task_actions.deny(req)

if res.task_actions_service_deny_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APITaskV1TaskActionsServiceDenyRequest](../../models/operations/c1apitaskv1taskactionsservicedenyrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.C1APITaskV1TaskActionsServiceDenyResponse](../../models/operations/c1apitaskv1taskactionsservicedenyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## escalate_to_emergency_access

Invokes the c1.api.task.v1.TaskActionsService.EscalateToEmergencyAccess method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessRequest(
    task_actions_service_escalate_to_emergency_access_request=shared.TaskActionsServiceEscalateToEmergencyAccessRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'string',
            ],
        ),
    ),
    task_id='string',
)

res = s.task_actions.escalate_to_emergency_access(req)

if res.task_service_action_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessRequest](../../models/operations/c1apitaskv1taskactionsserviceescalatetoemergencyaccessrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessResponse](../../models/operations/c1apitaskv1taskactionsserviceescalatetoemergencyaccessresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## restart

Invokes the c1.api.task.v1.TaskActionsService.Restart method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceRestartRequest(
    task_actions_service_restart_request=shared.TaskActionsServiceRestartRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'string',
            ],
        ),
    ),
    task_id='string',
)

res = s.task_actions.restart(req)

if res.task_actions_service_restart_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceRestartRequest](../../models/operations/c1apitaskv1taskactionsservicerestartrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APITaskV1TaskActionsServiceRestartResponse](../../models/operations/c1apitaskv1taskactionsservicerestartresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
