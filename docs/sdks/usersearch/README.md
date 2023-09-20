# UserSearch

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
            'aliquid',
        ],
    ),
    email='Hollie_Hirthe@gmail.com',
    exclude_ids=[
        'ab',
    ],
    ids=[
        'error',
    ],
    page_size=8224.07,
    page_token='voluptates',
    query='mollitia',
    refs=[
        shared.UserRef(
            id='ab5851d6-c645-4b08-b618-91baa0fe1ade',
        ),
    ],
    role_ids=[
        'voluptatem',
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

