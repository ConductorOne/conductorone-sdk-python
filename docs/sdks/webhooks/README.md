# Webhooks
(*webhooks*)

### Available Operations

* [test](#test) - Test

## test

Invokes the c1.api.webhooks.v1.WebhooksService.Test method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIWebhooksV1WebhooksServiceTestRequest(
    id='<id>',
)

res = s.webhooks.test(req)

if res.webhooks_service_test_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.C1APIWebhooksV1WebhooksServiceTestRequest](../../models/operations/c1apiwebhooksv1webhooksservicetestrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.C1APIWebhooksV1WebhooksServiceTestResponse](../../models/operations/c1apiwebhooksv1webhooksservicetestresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
