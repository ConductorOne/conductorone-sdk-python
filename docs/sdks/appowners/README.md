# app_owners

### Available Operations

* [add](#add) - Add
* [list](#list) - List
* [remove](#remove) - Remove

## add

Adds an owner to an app.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppOwnersAddRequest(
    add_app_owner_request=shared.AddAppOwnerRequest(),
    app_id='explicabo',
    user_id='deserunt',
)

res = s.app_owners.add(req)

if res.add_app_owner_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.C1APIAppV1AppOwnersAddRequest](../../models/operations/c1apiappv1appownersaddrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.C1APIAppV1AppOwnersAddResponse](../../models/operations/c1apiappv1appownersaddresponse.md)**


## list

List owners of an app.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppOwnersListRequest(
    app_id='distinctio',
    page_size=8413.86,
    page_token='labore',
)

res = s.app_owners.list(req)

if res.list_app_owners_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.C1APIAppV1AppOwnersListRequest](../../models/operations/c1apiappv1appownerslistrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.C1APIAppV1AppOwnersListResponse](../../models/operations/c1apiappv1appownerslistresponse.md)**


## remove

Removes an owner from an app.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIAppV1AppOwnersRemoveRequest(
    remove_app_owner_request=shared.RemoveAppOwnerRequest(),
    app_id='modi',
    user_id='qui',
)

res = s.app_owners.remove(req)

if res.remove_app_owner_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.C1APIAppV1AppOwnersRemoveRequest](../../models/operations/c1apiappv1appownersremoverequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.C1APIAppV1AppOwnersRemoveResponse](../../models/operations/c1apiappv1appownersremoveresponse.md)**

