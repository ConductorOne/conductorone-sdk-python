# TaskActions
(*task_actions*)

### Available Operations

* [approve](#approve) - Approve
* [comment](#comment) - Comment
* [deny](#deny) - Deny
* [escalate_to_emergency_access](#escalate_to_emergency_access) - Escalate To Emergency Access

## approve

Invokes the c1.api.task.v1.TaskActionsService.Approve method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceApproveRequest(
    task_actions_service_approve_request=shared.TaskActionsServiceApproveRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'Gasoline',
            ],
        ),
        comment='Carbonite web goalkeeper gloves are ergonomically designed to give easy fit',
        policy_step_id='synthesize Tennessee',
    ),
    task_id='Hatchback Northeast',
)

res = s.task_actions.approve(req)

if res.task_actions_service_approve_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceApproveRequest](../../models/operations/c1apitaskv1taskactionsserviceapproverequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APITaskV1TaskActionsServiceApproveResponse](../../models/operations/c1apitaskv1taskactionsserviceapproveresponse.md)**


## comment

Invokes the c1.api.task.v1.TaskActionsService.Comment method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceCommentRequest(
    task_actions_service_comment_request=shared.TaskActionsServiceCommentRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'Synergized',
            ],
        ),
        comment='The beautiful range of Apple Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients',
    ),
    task_id='enim than where',
)

res = s.task_actions.comment(req)

if res.task_actions_service_comment_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APITaskV1TaskActionsServiceCommentRequest](../../models/operations/c1apitaskv1taskactionsservicecommentrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APITaskV1TaskActionsServiceCommentResponse](../../models/operations/c1apitaskv1taskactionsservicecommentresponse.md)**


## deny

Invokes the c1.api.task.v1.TaskActionsService.Deny method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceDenyRequest(
    task_actions_service_deny_request=shared.TaskActionsServiceDenyRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'relationships',
            ],
        ),
        comment='The automobile layout consists of a front-engine design, with transaxle-type transmissions mounted at the rear of the engine and four wheel drive',
        policy_step_id='male',
    ),
    task_id='payment Pickup',
)

res = s.task_actions.deny(req)

if res.task_actions_service_deny_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.C1APITaskV1TaskActionsServiceDenyRequest](../../models/operations/c1apitaskv1taskactionsservicedenyrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.C1APITaskV1TaskActionsServiceDenyResponse](../../models/operations/c1apitaskv1taskactionsservicedenyresponse.md)**


## escalate_to_emergency_access

Invokes the c1.api.task.v1.TaskActionsService.EscalateToEmergencyAccess method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessRequest(
    task_actions_service_escalate_to_emergency_access_request=shared.TaskActionsServiceEscalateToEmergencyAccessRequest(
        task_expand_mask=shared.TaskExpandMask(
            paths=[
                'Practical',
            ],
        ),
        comment='The slim & simple Maple Gaming Keyboard from Dev Byte comes with a sleek body and 7- Color RGB LED Back-lighting for smart functionality',
        policy_step_id='invoice International',
    ),
    task_id='Southeast ethical',
)

res = s.task_actions.escalate_to_emergency_access(req)

if res.task_service_action_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessRequest](../../models/operations/c1apitaskv1taskactionsserviceescalatetoemergencyaccessrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.C1APITaskV1TaskActionsServiceEscalateToEmergencyAccessResponse](../../models/operations/c1apitaskv1taskactionsserviceescalatetoemergencyaccessresponse.md)**

