# WebhooksSearch
(*webhooks_search*)

## Overview

### Available Operations

* [search](#search) - Search

## search

Invokes the c1.api.webhooks.v1.WebhooksSearch.Search method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.webhooks.v1.WebhooksSearch.Search" method="post" path="/api/v1/search/webhooks" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.webhooks_search.search(request={})

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.WebhooksSearchRequest](../../models/shared/webhookssearchrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.C1APIWebhooksV1WebhooksSearchSearchResponse](../../models/operations/c1apiwebhooksv1webhookssearchsearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |