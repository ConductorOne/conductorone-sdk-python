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
        bearer_auth="",
        oauth="",
    ),
)

req = shared.SearchUsersRequest(
    user_expand_mask=shared.UserExpandMask(
        paths=[
            'officia',
        ],
    ),
    email='Green.Bahringer@yahoo.com',
    exclude_ids=[
        'iste',
    ],
    ids=[
        'id',
    ],
    page_size=700.42,
    page_token='error',
    query='possimus',
    refs=[
        shared.UserRef(
            id='eaab5851-d6c6-445b-88b6-1891baa0fe1a',
        ),
    ],
    role_ids=[
        'pariatur',
    ],
    user_statuses=[
        shared.SearchUsersRequestUserStatuses.DELETED,
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

