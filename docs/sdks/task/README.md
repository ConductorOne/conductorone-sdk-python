# task

### Available Operations

* [create_grant_task](#create_grant_task) - Create Grant Task
* [create_revoke_task](#create_revoke_task) - Create Revoke Task
* [get](#get) - Get

## create_grant_task

Create a grant task

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = shared.TaskServiceCreateGrantRequest(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'soluta',
        ],
    ),
    app_entitlement_id='repudiandae',
    app_id='nam',
    app_user_id='dolore',
    description='iusto',
    emergency_access=False,
    grant_duration='voluptate',
    identity_user_id='sequi',
)

res = s.task.create_grant_task(req)

if res.task_service_create_grant_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.TaskServiceCreateGrantRequest](../../models/shared/taskservicecreategrantrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.C1APITaskV1TaskServiceCreateGrantTaskResponse](../../models/operations/c1apitaskv1taskservicecreategranttaskresponse.md)**


## create_revoke_task

Create a revoke task

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = shared.TaskServiceCreateRevokeRequest(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'neque',
            'quo',
        ],
    ),
    app_entitlement_id='deleniti',
    app_id='quibusdam',
    app_user_id='iure',
    description='odit',
    identity_user_id='voluptatibus',
)

res = s.task.create_revoke_task(req)

if res.task_service_create_revoke_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [shared.TaskServiceCreateRevokeRequest](../../models/shared/taskservicecreaterevokerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.C1APITaskV1TaskServiceCreateRevokeTaskResponse](../../models/operations/c1apitaskv1taskservicecreaterevoketaskresponse.md)**


## get

Get a task by ID

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APITaskV1TaskServiceGetRequest(
    id='64d1db1f-2c43-4106-a1e9-6349e1cf9e06',
)

res = s.task.get(req)

if res.task_service_get_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.C1APITaskV1TaskServiceGetRequest](../../models/operations/c1apitaskv1taskservicegetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.C1APITaskV1TaskServiceGetResponse](../../models/operations/c1apitaskv1taskservicegetresponse.md)**

