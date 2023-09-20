# PolicySearch

### Available Operations

* [search](#search) - Search

## search

Search policies based on filters specified in the request body.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.SearchPoliciesRequest(
    display_name='natus',
    page_size=2446.51,
    page_token='voluptatibus',
    policy_types=[
        shared.SearchPoliciesRequestPolicyTypes.POLICY_TYPE_REVOKE,
    ],
    query='asperiores',
    refs=[
        shared.PolicyRef(
            id='0642dac7-af51-45cc-813a-a63aae8d6786',
        ),
    ],
)

res = s.policy_search.search(req)

if res.list_policy_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.SearchPoliciesRequest](../../models/shared/searchpoliciesrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.C1APIPolicyV1PolicySearchSearchResponse](../../models/operations/c1apipolicyv1policysearchsearchresponse.md)**

