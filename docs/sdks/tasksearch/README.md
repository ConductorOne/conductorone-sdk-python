# TaskSearch
(*task_search*)

### Available Operations

* [search](#search) - Search

## search

Search tasks based on filters specified in the request body.

### Example Usage

```python
import dateutil.parser
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = shared.TaskSearchRequest(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'string',
        ],
    ),
    access_review_ids=[
        'string',
    ],
    account_owner_ids=[
        'string',
    ],
    app_entitlement_ids=[
        'string',
    ],
    app_resource_ids=[
        'string',
    ],
    app_resource_type_ids=[
        'string',
    ],
    app_user_subject_ids=[
        'string',
    ],
    application_ids=[
        'string',
    ],
    assignees_in_ids=[
        'string',
    ],
    exclude_app_entitlement_ids=[
        'string',
    ],
    exclude_ids=[
        'string',
    ],
    my_work_user_ids=[
        'string',
    ],
    opener_ids=[
        'string',
    ],
    previously_acted_on_ids=[
        'string',
    ],
    refs=[
        shared.TaskRef(),
    ],
    subject_ids=[
        'string',
    ],
    task_states=[
        shared.TaskStates.TASK_STATE_UNSPECIFIED,
    ],
    task_types=[
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertifyInput(),
            task_type_grant=shared.TaskTypeGrantInput(
                task_grant_source=shared.TaskGrantSource(),
            ),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(),
                ),
            ),
        ),
    ],
)

res = s.task_search.search(req)

if res.task_search_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.TaskSearchRequest](../../models/shared/tasksearchrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.C1APITaskV1TaskSearchServiceSearchResponse](../../models/operations/c1apitaskv1tasksearchservicesearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
