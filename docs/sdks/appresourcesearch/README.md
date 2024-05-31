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
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.app_resource_search.search_app_resource_types(request=shared.SearchAppResourceTypesRequest())

if res.search_app_resource_types_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.SearchAppResourceTypesRequest](../../models/shared/searchappresourcetypesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.C1APIAppV1AppResourceSearchSearchAppResourceTypesResponse](../../models/operations/c1apiappv1appresourcesearchsearchappresourcetypesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
