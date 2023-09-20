# AppResourceSearch

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
        'explicabo',
    ],
    exclude_resource_type_ids=[
        'deserunt',
    ],
    exclude_resource_type_trait_ids=[
        'distinctio',
    ],
    page_size=8413.86,
    page_token='labore',
    query='modi',
    resource_type_ids=[
        'qui',
    ],
    resource_type_trait_ids=[
        'aliquid',
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

