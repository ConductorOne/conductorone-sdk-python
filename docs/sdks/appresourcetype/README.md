# AppResourceType
(*.app_resource_type*)

### Available Operations

* [get](#get) - Get
* [list](#list) - List

## get

Get an app resource type.

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

req = operations.C1APIAppV1AppResourceTypeServiceGetRequest(
    app_id='string',
    id='<ID>',
)

res = s.app_resource_type.get(req)

if res.app_resource_type_service_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.C1APIAppV1AppResourceTypeServiceGetRequest](../../models/operations/c1apiappv1appresourcetypeservicegetrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.C1APIAppV1AppResourceTypeServiceGetResponse](../../models/operations/c1apiappv1appresourcetypeservicegetresponse.md)**


## list

List app resource types.

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

req = operations.C1APIAppV1AppResourceTypeServiceListRequest(
    app_id='string',
)

res = s.app_resource_type.list(req)

if res.app_resource_type_service_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppResourceTypeServiceListRequest](../../models/operations/c1apiappv1appresourcetypeservicelistrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APIAppV1AppResourceTypeServiceListResponse](../../models/operations/c1apiappv1appresourcetypeservicelistresponse.md)**

