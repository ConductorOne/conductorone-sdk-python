# WebhooksSearch
(*webhooks_search*)

### Available Operations

* [search](#search) - Search

## search

Invokes the c1.api.webhooks.v1.WebhooksSearch.Search method.

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


res = s.webhooks_search.search(request=shared.WebhooksSearchRequest())

if res.webhooks_search_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.WebhooksSearchRequest](../../models/shared/webhookssearchrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.C1APIWebhooksV1WebhooksSearchSearchResponse](../../models/operations/c1apiwebhooksv1webhookssearchsearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
