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
    display_name='voluptas',
    page_size=9903.45,
    page_token='aperiam',
    policy_types=[
        shared.SearchPoliciesRequestPolicyTypes.POLICY_TYPE_REVOKE,
    ],
    query='quaerat',
    refs=[
        shared.PolicyRef(
            id='2dac7af5-15cc-4413-aa63-aae8d67864db',
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

