# PersonalClientSearch
(*personal_client_search*)

## Overview

### Available Operations

* [search](#search) - NOTE: Searches personal clients for all users

## search

Invokes the c1.api.iam.v1.PersonalClientSearchService.Search method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.PersonalClientSearchService.Search" method="post" path="/api/v1/search/iam/personal_clients" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.personal_client_search.search()

    assert res.personal_client_search_service_search_response is not None

    # Handle response
    print(res.personal_client_search_service_search_response)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [shared.PersonalClientSearchServiceSearchRequest](../../models/shared/personalclientsearchservicesearchrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.C1APIIamV1PersonalClientSearchServiceSearchResponse](../../models/operations/c1apiiamv1personalclientsearchservicesearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |