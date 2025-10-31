# RequestCatalogSearch
(*request_catalog_search*)

## Overview

### Available Operations

* [search_entitlements](#search_entitlements) - Search Entitlements

## search_entitlements

Search request catalogs based on filters specified in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogSearchService.SearchEntitlements" method="post" path="/api/v1/search/request_catalog/entitlements" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.request_catalog_search.search_entitlements(request={})

    assert res.request_catalog_search_service_search_entitlements_response is not None

    # Handle response
    print(res.request_catalog_search_service_search_entitlements_response)

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [shared.RequestCatalogSearchServiceSearchEntitlementsRequest](../../models/shared/requestcatalogsearchservicesearchentitlementsrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |
| `retries`                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                           | :heavy_minus_sign:                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                        |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogSearchServiceSearchEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogsearchservicesearchentitlementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |