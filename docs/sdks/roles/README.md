# roles

### Available Operations

* [get](#get) - Get
* [list](#list) - List
* [update](#update) - Update

## get

Get a role by id.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIIamV1RolesGetRequest(
    role_id='necessitatibus',
)

res = s.roles.get(req)

if res.get_roles_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.C1APIIamV1RolesGetRequest](../../models/operations/c1apiiamv1rolesgetrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.C1APIIamV1RolesGetResponse](../../models/operations/c1apiiamv1rolesgetresponse.md)**


## list

List all roles for the current user.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIIamV1RolesListRequest(
    page_size=9918.91,
    page_token='ex',
)

res = s.roles.list(req)

if res.list_roles_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.C1APIIamV1RolesListRequest](../../models/operations/c1apiiamv1roleslistrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.C1APIIamV1RolesListResponse](../../models/operations/c1apiiamv1roleslistresponse.md)**


## update

Update a role by passing a Role object.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIIamV1RolesUpdateRequest(
    update_role_request_input=shared.UpdateRoleRequestInput(
        role=shared.RoleInput(
            display_name='voluptas',
            permissions=[
                'delectus',
                'quae',
                'minus',
                'fuga',
            ],
            service_roles=[
                'consectetur',
                'velit',
                'atque',
            ],
        ),
        update_mask='ipsum',
    ),
    role_id='impedit',
)

res = s.roles.update(req)

if res.update_roles_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.C1APIIamV1RolesUpdateRequest](../../models/operations/c1apiiamv1rolesupdaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.C1APIIamV1RolesUpdateResponse](../../models/operations/c1apiiamv1rolesupdateresponse.md)**

