# FunctionsSearch
(*functions_search*)

## Overview

### Available Operations

* [search](#search) - Search

## search

Search searches for functions based on criteria

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.functions.v1.FunctionsSearch.Search" method="post" path="/api/v1/search/functions" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.functions_search.search(request={})

    assert res.functions_search_response is not None

    # Handle response
    print(res.functions_search_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.FunctionsSearchRequest](../../models/shared/functionssearchrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.C1APIFunctionsV1FunctionsSearchSearchResponse](../../models/operations/c1apifunctionsv1functionssearchsearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |