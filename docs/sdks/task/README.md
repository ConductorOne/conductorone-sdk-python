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
        bearer_auth="",
        oauth="",
    ),
)

req = shared.TaskServiceCreateGrantRequest(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'totam',
        ],
    ),
    task_grant_source=shared.TaskGrantSource(
        external_url='quae',
        integration_id='molestiae',
    ),
    app_entitlement_id='eveniet',
    app_id='qui',
    app_user_id='cum',
    description='iure',
    emergency_access=False,
    grant_duration='necessitatibus',
    identity_user_id='ratione',
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
        bearer_auth="",
        oauth="",
    ),
)

req = shared.TaskServiceCreateRevokeRequest(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'laborum',
        ],
    ),
    app_entitlement_id='distinctio',
    app_id='voluptatum',
    app_user_id='rem',
    description='aliquam',
    identity_user_id='ad',
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
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APITaskV1TaskServiceGetRequest(
    id='f0597a60-ff2a-454a-b1e9-4764a3e865e7',
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

