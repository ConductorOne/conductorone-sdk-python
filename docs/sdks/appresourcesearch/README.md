# AppResourceSearch
(*app_resource_search*)

### Available Operations

* [search_app_resource_types](#search_app_resource_types) - Search App Resource Types

## search_app_resource_types

Search app resources based on filters specified in the request body.

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

req = shared.SearchAppResourceTypesRequest(
    app_ids=[
        'Soap',
    ],
    exclude_resource_type_ids=[
        'paradigms',
    ],
    exclude_resource_type_trait_ids=[
        'World',
    ],
    page_size=553.23,
    page_token='SUV nostrum specifically',
    query='Distributed across',
    resource_type_ids=[
        'minima',
    ],
    resource_type_trait_ids=[
        'Branding',
    ],
)

res = s.app_resource_search.search_app_resource_types(req)

if res.search_app_resource_types_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.SearchAppResourceTypesRequest](../../models/shared/searchappresourcetypesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.C1APIAppV1AppResourceSearchSearchAppResourceTypesResponse](../../models/operations/c1apiappv1appresourcesearchsearchappresourcetypesresponse.md)**

