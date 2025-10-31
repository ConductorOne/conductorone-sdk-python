# AccountProvisionPolicyTest
(*account_provision_policy_test*)

## Overview

### Available Operations

* [test](#test) - Test

## test

Invokes the c1.api.policy.v1.AccountProvisionPolicyTest.Test method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.policy.v1.AccountProvisionPolicyTest.Test" method="post" path="/api/v1/policies/test-account-provision-policy" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.account_provision_policy_test.test(request={})

    assert res.test_account_provision_policy_response is not None

    # Handle response
    print(res.test_account_provision_policy_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.TestAccountProvisionPolicyRequest](../../models/shared/testaccountprovisionpolicyrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.C1APIPolicyV1AccountProvisionPolicyTestTestResponse](../../models/operations/c1apipolicyv1accountprovisionpolicytesttestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |