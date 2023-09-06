# app_resource_owners

### Available Operations

* [list](#list) - List

## list

List all owners of an app resource.

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

req = operations.C1APIAppV1AppResourceOwnersListRequest(
    app_id='incidunt',
    page_size=3185.69,
    page_token='consequatur',
    resource_id='est',
    resource_type_id='quibusdam',
)

res = s.app_resource_owners.list(req)

if res.list_app_resource_owners_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.C1APIAppV1AppResourceOwnersListRequest](../../models/operations/c1apiappv1appresourceownerslistrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.C1APIAppV1AppResourceOwnersListResponse](../../models/operations/c1apiappv1appresourceownerslistresponse.md)**

