# app_search

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
        'cumque',
    ],
    display_name='facere',
    exclude_app_ids=[
        'ea',
    ],
    page_size=3965.06,
    page_token='laborum',
    query='accusamus',
)

res = s.app_search.search(req)

if res.search_apps_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.SearchAppsRequest](../../models/shared/searchappsrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.C1APIAppV1AppSearchSearchResponse](../../models/operations/c1apiappv1appsearchsearchresponse.md)**

