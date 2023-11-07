# Roles
(*.roles*)

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
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIIamV1RolesGetRequest(
    role_id='string',
)

res = s.roles.get(req)

if res.get_roles_response is not None:
    # handle response
    pass
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
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIIamV1RolesListRequest()

res = s.roles.list(req)

if res.list_roles_response is not None:
    # handle response
    pass
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
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIIamV1RolesUpdateRequest(
    update_role_request=shared.UpdateRoleRequest(
        role=shared.RoleInput(
            permissions=[
                'string',
            ],
            service_roles=[
                'string',
            ],
        ),
    ),
    role_id='string',
)

res = s.roles.update(req)

if res.update_roles_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.C1APIIamV1RolesUpdateRequest](../../models/operations/c1apiiamv1rolesupdaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.C1APIIamV1RolesUpdateResponse](../../models/operations/c1apiiamv1rolesupdateresponse.md)**

