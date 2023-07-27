# app_resource_type

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
        oauth="",
    ),
)

req = operations.C1APIAppV1AppResourceTypeServiceGetRequest(
    app_id='natus',
    id='b6e21419-5989-40af-a563-e2516fe4c8b7',
)

res = s.app_resource_type.get(req)

if res.app_resource_type_service_get_response is not None:
    # handle response
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
        oauth="",
    ),
)

req = operations.C1APIAppV1AppResourceTypeServiceListRequest(
    app_id='architecto',
    page_size=995.69,
    page_token='repudiandae',
)

res = s.app_resource_type.list(req)

if res.app_resource_type_service_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIAppV1AppResourceTypeServiceListRequest](../../models/operations/c1apiappv1appresourcetypeservicelistrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APIAppV1AppResourceTypeServiceListResponse](../../models/operations/c1apiappv1appresourcetypeservicelistresponse.md)**

