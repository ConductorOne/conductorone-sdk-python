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
    email='Jadyn.Goyette43@hotmail.com',
    exclude_ids=[
        'Hyundai',
    ],
    ids=[
        'Future',
    ],
    page_size=1145.76,
    page_token='broach dependent Mozambique',
    query='eligendi Tobago',
    refs=[
        shared.UserRef(
            id='<ID>',
        ),
    ],
    role_ids=[
        'Protactinium',
    ],
    user_statuses=[
        shared.SearchUsersRequestUserStatuses.DISABLED,
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

