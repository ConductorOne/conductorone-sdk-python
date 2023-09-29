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
    actor_id='Practical yearningly Southeast',
    app_entitlement_ids=[
        'Books',
    ],
    app_resource_ids=[
        'Other',
    ],
    app_resource_type_ids=[
        'eligendi',
    ],
    app_user_subject_ids=[
        'Tobago',
    ],
    application_ids=[
        'Protactinium',
    ],
    assignees_in_ids=[
        'Arsenic',
    ],
    created_after=dateutil.parser.isoparse('2023-06-10T20:22:45.491Z'),
    created_before=dateutil.parser.isoparse('2022-09-06T19:12:57.415Z'),
    current_step=shared.TaskSearchRequestCurrentStep.TASK_SEARCH_CURRENT_STEP_UNSPECIFIED,
    emergency_status=shared.TaskSearchRequestEmergencyStatus.NON_EMERGENCY,
    exclude_app_entitlement_ids=[
        'National',
    ],
    exclude_ids=[
        'Wagon',
    ],
    include_deleted=False,
    my_work_user_ids=[
        'Estate',
    ],
    opener_ids=[
        'female',
    ],
    page_size=2339.71,
    page_token='Soft Bacon',
    previously_acted_on_ids=[
        'mindshare',
    ],
    query='frizzy',
    refs=[
        shared.TaskRef(
            id='<ID>',
        ),
    ],
    sort_by=shared.TaskSearchRequestSortBy.TASK_SEARCH_SORT_BY_ACCOUNT_OWNER,
    subject_ids=[
        'boo',
    ],
    task_states=[
        shared.TaskSearchRequestTaskStates.TASK_STATE_UNSPECIFIED,
    ],
    task_types=[
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertifyInput(),
            task_type_grant=shared.TaskTypeGrantInput(
                task_grant_source=shared.TaskGrantSource(
                    external_url='Frozen',
                    integration_id='discrete HDD chargrill',
                ),
            ),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(
                        expired_at=dateutil.parser.isoparse('2023-03-10T15:48:59.869Z'),
                    ),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(
                        expires_at=dateutil.parser.isoparse('2023-01-14T01:21:25.379Z'),
                        last_login=dateutil.parser.isoparse('2021-01-22T06:17:27.525Z'),
                    ),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(
                        request_user_id='overriding Focused',
                    ),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(
                        access_review_id='plum Astatine',
                        cert_ticket_id='soliloquize instead',
                    ),
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

