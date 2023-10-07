# TaskSearch
(*task_search*)

### Available Operations

* [search](#search) - Search

## search

Search tasks based on filters specified in the request body.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.TaskSearchRequestInput(
    task_expand_mask=shared.TaskExpandMask(
        paths=[
            'transition',
        ],
    ),
    access_review_ids=[
        'turquoise',
    ],
    account_owner_ids=[
        'Hyundai',
    ],
    app_entitlement_ids=[
        'Future',
    ],
    app_resource_ids=[
        'Southwest',
    ],
    app_resource_type_ids=[
        'broach',
    ],
    app_user_subject_ids=[
        'dependent',
    ],
    application_ids=[
        'Mozambique',
    ],
    assignees_in_ids=[
        'Global',
    ],
    exclude_app_entitlement_ids=[
        'watt',
    ],
    exclude_ids=[
        'Gasoline',
    ],
    my_work_user_ids=[
        'Protactinium',
    ],
    opener_ids=[
        'Arsenic',
    ],
    previously_acted_on_ids=[
        'Gasoline',
    ],
    refs=[
        shared.TaskRef(),
    ],
    subject_ids=[
        'Oklahoma',
    ],
    task_states=[
        shared.TaskSearchRequestTaskStates.TASK_STATE_UNSPECIFIED,
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
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.TaskSearchRequestInput](../../models/shared/tasksearchrequestinput.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.C1APITaskV1TaskSearchServiceSearchResponse](../../models/operations/c1apitaskv1tasksearchservicesearchresponse.md)**

