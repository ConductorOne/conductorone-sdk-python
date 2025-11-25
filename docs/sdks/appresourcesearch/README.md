# AppResourceSearch
(*app_resource_search*)

## Overview

### Available Operations

* [search_app_resource_types](#search_app_resource_types) - Search App Resource Types
* [search_app_resources](#search_app_resources) - Search App Resources

## search_app_resource_types

Search app resources based on filters specified in the request body.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceSearch.SearchAppResourceTypes" method="post" path="/api/v1/search/app_resource_types" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_search.search_app_resource_types()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.SearchAppResourceTypesRequest](../../models/shared/searchappresourcetypesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.C1APIAppV1AppResourceSearchSearchAppResourceTypesResponse](../../models/operations/c1apiappv1appresourcesearchsearchappresourcetypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search_app_resources

Invokes the c1.api.app.v1.AppResourceSearch.SearchAppResources method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.app.v1.AppResourceSearch.SearchAppResources" method="post" path="/api/v1/search/app_resources" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_resource_search.search_app_resources()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.SearchAppResourcesRequest](../../models/shared/searchappresourcesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.C1APIAppV1AppResourceSearchSearchAppResourcesResponse](../../models/operations/c1apiappv1appresourcesearchsearchappresourcesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |