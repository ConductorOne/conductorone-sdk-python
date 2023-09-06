# apps

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - List
* [update](#update) - Update

## create

Create a new app.

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

req = shared.CreateAppRequest(
    certify_policy_id='sapiente',
    description='amet',
    display_name='deserunt',
    grant_policy_id='nisi',
    monthly_cost_usd=4238.55,
    owners=[
        'natus',
    ],
    revoke_policy_id='omnis',
)

res = s.apps.create(req)

if res.create_app_response is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.CreateAppRequest](../../models/shared/createapprequest.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.C1APIAppV1AppsCreateResponse](../../models/operations/c1apiappv1appscreateresponse.md)**


## delete

Delete an app.

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

req = operations.C1APIAppV1AppsDeleteRequest(
    delete_app_request=shared.DeleteAppRequest(),
    id='7074ba44-69b6-4e21-8195-9890afa563e2',
)

res = s.apps.delete(req)

if res.delete_app_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.C1APIAppV1AppsDeleteRequest](../../models/operations/c1apiappv1appsdeleterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.C1APIAppV1AppsDeleteResponse](../../models/operations/c1apiappv1appsdeleteresponse.md)**


## get

Get an app by ID.

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

req = operations.C1APIAppV1AppsGetRequest(
    id='516fe4c8-b711-4e5b-bfd2-ed028921cddc',
)

res = s.apps.get(req)

if res.get_app_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.C1APIAppV1AppsGetRequest](../../models/operations/c1apiappv1appsgetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.C1APIAppV1AppsGetResponse](../../models/operations/c1apiappv1appsgetresponse.md)**


## list

List all apps.

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

req = operations.C1APIAppV1AppsListRequest(
    page_size=4113.97,
    page_token='excepturi',
)

res = s.apps.list(req)

if res.list_apps_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.C1APIAppV1AppsListRequest](../../models/operations/c1apiappv1appslistrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.C1APIAppV1AppsListResponse](../../models/operations/c1apiappv1appslistresponse.md)**


## update

Update an existing app.

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

req = operations.C1APIAppV1AppsUpdateRequest(
    update_app_request_input=shared.UpdateAppRequestInput(
        app=shared.AppInput(
            certify_policy_id='odit',
            description='ea',
            display_name='accusantium',
            grant_policy_id='ab',
            icon_url='maiores',
            monthly_cost_usd=6974.29,
            revoke_policy_id='ipsam',
        ),
        update_mask='voluptate',
    ),
    id='6b0d5f0d-30c5-4fbb-a587-053202c73d5f',
)

res = s.apps.update(req)

if res.update_app_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.C1APIAppV1AppsUpdateRequest](../../models/operations/c1apiappv1appsupdaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.C1APIAppV1AppsUpdateResponse](../../models/operations/c1apiappv1appsupdateresponse.md)**

