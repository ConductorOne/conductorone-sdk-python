# StepUpTransaction
(*step_up_transaction*)

## Overview

### Available Operations

* [get](#get) - Get
* [search](#search) - Search

## get

Get retrieves a specific step-up transaction by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpTransactionService.Get" method="get" path="/api/v1/step-up/transactions/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.step_up_transaction.get(request={
        "id": "<id>",
    })

    assert res.get_step_up_transaction_response is not None

    # Handle response
    print(res.get_step_up_transaction_response)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.C1APIStepupV1StepUpTransactionServiceGetRequest](../../models/operations/c1apistepupv1stepuptransactionservicegetrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[operations.C1APIStepupV1StepUpTransactionServiceGetResponse](../../models/operations/c1apistepupv1stepuptransactionservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search

Search allows searching for step-up transactions with various filters

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.stepup.v1.StepUpTransactionService.Search" method="post" path="/api/v1/search/step-up/transactions" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.step_up_transaction.search()

    assert res.search_step_up_transactions_response is not None

    # Handle response
    print(res.search_step_up_transactions_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.SearchStepUpTransactionsRequest](../../models/shared/searchstepuptransactionsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.C1APIStepupV1StepUpTransactionServiceSearchResponse](../../models/operations/c1apistepupv1stepuptransactionservicesearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |