# user_search

### Available Operations

* [search](#search) - Search

## search

Search users based on filters specified in the request body.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = shared.SearchUsersRequest(
    user_expand_mask=shared.UserExpandMask(
        paths=[
            'impedit',
            'delectus',
            'tempore',
        ],
    ),
    email='Bruce.Zieme44@hotmail.com',
    exclude_ids=[
        'odio',
    ],
    ids=[
        'in',
        'ducimus',
    ],
    page_size=5678.46,
    page_token='dolores',
    query='error',
    refs=[
        shared.UserRef(
            id='77deac64-6ecb-4573-809e-3eb1e5a2b12e',
        ),
    ],
    role_ids=[
        'ipsa',
        'ducimus',
        'maiores',
    ],
    user_statuses=[
        shared.SearchUsersRequestUserStatuses.UNKNOWN,
    ],
)

res = s.user_search.search(req)

if res.search_users_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.SearchUsersRequest](../../models/shared/searchusersrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.C1APIUserV1UserSearchSearchResponse](../../models/operations/c1apiuserv1usersearchsearchresponse.md)**

