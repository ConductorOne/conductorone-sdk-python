# AppOwners
(*app_owners*)

### Available Operations

* [add](#add) - Add
* [list](#list) - List
* [remove](#remove) - Remove
* [set](#set) - Set

## add

Adds an owner to an app.

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

req = operations.C1APIAppV1AppOwnersAddRequest(
    add_app_owner_request=shared.AddAppOwnerRequest(),
    app_id='string',
    user_id='string',
)

res = s.app_owners.add(req)

if res.add_app_owner_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.C1APIAppV1AppOwnersAddRequest](../../models/operations/c1apiappv1appownersaddrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.C1APIAppV1AppOwnersAddResponse](../../models/operations/c1apiappv1appownersaddresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list

List owners of an app.

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

req = operations.C1APIAppV1AppOwnersListRequest(
    app_id='string',
)

res = s.app_owners.list(req)

if res.list_app_owners_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.C1APIAppV1AppOwnersListRequest](../../models/operations/c1apiappv1appownerslistrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.C1APIAppV1AppOwnersListResponse](../../models/operations/c1apiappv1appownerslistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove

Removes an owner from an app.

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

req = operations.C1APIAppV1AppOwnersRemoveRequest(
    remove_app_owner_request=shared.RemoveAppOwnerRequest(),
    app_id='string',
    user_id='string',
)

res = s.app_owners.remove(req)

if res.remove_app_owner_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.C1APIAppV1AppOwnersRemoveRequest](../../models/operations/c1apiappv1appownersremoverequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.C1APIAppV1AppOwnersRemoveResponse](../../models/operations/c1apiappv1appownersremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## set

Sets the owners for a given app to the specified list of users.

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

req = operations.C1APIAppV1AppOwnersSetRequest(
    set_app_owners_request=shared.SetAppOwnersRequest(
        user_ids=[
            'string',
        ],
    ),
    app_id='string',
)

res = s.app_owners.set(req)

if res.set_app_owners_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.C1APIAppV1AppOwnersSetRequest](../../models/operations/c1apiappv1appownerssetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.C1APIAppV1AppOwnersSetResponse](../../models/operations/c1apiappv1appownerssetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
