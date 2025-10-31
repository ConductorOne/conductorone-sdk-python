# PolicyValidate
(*policy_validate*)

## Overview

### Available Operations

* [validate_cel](#validate_cel) - Validate Cel

## validate_cel

Validate policies

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.policy.v1.PolicyValidate.ValidateCEL" method="post" path="/api/v1/policies/validate/cel" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.policy_validate.validate_cel(request={})

    assert res.editor_validate_response is not None

    # Handle response
    print(res.editor_validate_response)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.EditorValidateRequest](../../models/shared/editorvalidaterequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.C1APIPolicyV1PolicyValidateValidateCELResponse](../../models/operations/c1apipolicyv1policyvalidatevalidatecelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |