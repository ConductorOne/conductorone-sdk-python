# user

### Available Operations

* [get](#get) - Get
* [list](#list) - List

## get

Get a user by ID.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIUserV1UserServiceGetRequest(
    id='7ce52b89-5c53-47c6-854e-fb0b34896c3c',
)

res = s.user.get(req)

if res.user_service_get_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.C1APIUserV1UserServiceGetRequest](../../models/operations/c1apiuserv1userservicegetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.C1APIUserV1UserServiceGetResponse](../../models/operations/c1apiuserv1userservicegetresponse.md)**


## list

List users.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIUserV1UserServiceListRequest(
    page_size=6845.53,
    page_token='nostrum',
)

res = s.user.list(req)

if res.user_service_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.C1APIUserV1UserServiceListRequest](../../models/operations/c1apiuserv1userservicelistrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.C1APIUserV1UserServiceListResponse](../../models/operations/c1apiuserv1userservicelistresponse.md)**

