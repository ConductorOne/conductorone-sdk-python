# policy_search

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
        oauth="",
    ),
)

req = shared.SearchPoliciesRequest(
    display_name='hic',
    page_size=3487.83,
    page_token='nobis',
    policy_types=[
        shared.SearchPoliciesRequestPolicyTypes.POLICY_TYPE_ACCESS_REQUEST,
    ],
    query='sed',
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

