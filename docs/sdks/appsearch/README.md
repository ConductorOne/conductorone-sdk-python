# AppSearch
(*app_search*)

### Available Operations

* [search](#search) - Search

## search

Search apps based on filters specified in the request body.

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

req = shared.SearchAppsRequest(
    app_ids=[
        'string',
    ],
    exclude_app_ids=[
        'string',
    ],
)

res = s.app_search.search(req)

if res.search_apps_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.SearchAppsRequest](../../models/shared/searchappsrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.C1APIAppV1AppSearchSearchResponse](../../models/operations/c1apiappv1appsearchsearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
