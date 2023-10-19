# UserSearch
(*user_search*)

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
        bearer_auth="",
        oauth="",
    ),
)

req = shared.SearchUsersRequest(
    user_expand_mask=shared.UserExpandMask(
        paths=[
            'transition',
        ],
    ),
    exclude_ids=[
        'turquoise',
    ],
    ids=[
        'Hyundai',
    ],
    refs=[
        shared.UserRef(),
    ],
    role_ids=[
        'Future',
    ],
    user_statuses=[
        shared.SearchUsersRequestUserStatuses.UNKNOWN,
    ],
)

res = s.user_search.search(req)

if res.search_users_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.SearchUsersRequest](../../models/shared/searchusersrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.C1APIUserV1UserSearchSearchResponse](../../models/operations/c1apiuserv1usersearchsearchresponse.md)**

