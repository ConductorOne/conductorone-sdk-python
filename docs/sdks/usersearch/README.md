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
            'voluptas',
        ],
    ),
    email='Maiya_Bernier@yahoo.com',
    exclude_ids=[
        'voluptates',
    ],
    ids=[
        'mollitia',
    ],
    page_size=6717.94,
    page_token='libero',
    query='ad',
    refs=[
        shared.UserRef(
            id='851d6c64-5b08-4b61-891b-aa0fe1ade008',
        ),
    ],
    role_ids=[
        'earum',
    ],
    user_statuses=[
        shared.SearchUsersRequestUserStatuses.ENABLED,
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

