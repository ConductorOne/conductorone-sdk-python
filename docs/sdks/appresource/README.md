# AppResource
(*app_resource*)

### Available Operations

* [get](#get) - Get
* [list](#list) - List

## get

Invokes the c1.api.app.v1.AppResourceService.Get method.

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

req = operations.C1APIAppV1AppResourceServiceGetRequest(
    app_id='Group Cambridgeshire',
    app_resource_type_id='reintermediate fuchsia Planner',
    id='<ID>',
)

res = s.app_resource.get(req)

if res.app_resource_service_get_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppResourceServiceGetRequest](../../models/operations/c1apiappv1appresourceservicegetrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.C1APIAppV1AppResourceServiceGetResponse](../../models/operations/c1apiappv1appresourceservicegetresponse.md)**


## list

Invokes the c1.api.app.v1.AppResourceService.List method.

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

req = operations.C1APIAppV1AppResourceServiceListRequest(
    app_id='Bronze Architect',
    app_resource_type_id='Southeast Soap katal',
    page_size=4900.99,
    page_token='aftermath',
)

res = s.app_resource.list(req)

if res.app_resource_service_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1AppResourceServiceListRequest](../../models/operations/c1apiappv1appresourceservicelistrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.C1APIAppV1AppResourceServiceListResponse](../../models/operations/c1apiappv1appresourceservicelistresponse.md)**

