# ExportsSearch
(*exports_search*)

## Overview

### Available Operations

* [search](#search) - Search

## search

Invokes the c1.api.systemlog.v1.ExportsSearchService.Search method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.systemlog.v1.ExportsSearchService.Search" method="post" path="/api/v1/search/systemlog/exports" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.exports_search.search(request={})

    assert res.exports_search_service_search_response is not None

    # Handle response
    print(res.exports_search_service_search_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.ExportsSearchServiceSearchRequest](../../models/shared/exportssearchservicesearchrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.C1APISystemlogV1ExportsSearchServiceSearchResponse](../../models/operations/c1apisystemlogv1exportssearchservicesearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |