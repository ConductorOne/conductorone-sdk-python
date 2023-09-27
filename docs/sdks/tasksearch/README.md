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
            'in',
        ],
    ),
    access_review_ids=[
        'nam',
    ],
    account_owner_ids=[
        'earum',
    ],
    actor_id='officia',
    app_entitlement_ids=[
        'laborum',
    ],
    app_resource_ids=[
        'placeat',
    ],
    app_resource_type_ids=[
        'modi',
    ],
    app_user_subject_ids=[
        'voluptatibus',
    ],
    application_ids=[
        'molestias',
    ],
    assignees_in_ids=[
        'officiis',
    ],
    created_after=dateutil.parser.isoparse('2020-09-15T19:18:40.244Z'),
    created_before=dateutil.parser.isoparse('2022-04-21T03:20:35.575Z'),
    current_step=shared.TaskSearchRequestCurrentStep.TASK_SEARCH_CURRENT_STEP_UNSPECIFIED,
    emergency_status=shared.TaskSearchRequestEmergencyStatus.ALL,
    exclude_app_entitlement_ids=[
        'inventore',
    ],
    exclude_ids=[
        'fugit',
    ],
    include_deleted=False,
    my_work_user_ids=[
        'cumque',
    ],
    opener_ids=[
        'quae',
    ],
    page_size=216.88,
    page_token='velit',
    previously_acted_on_ids=[
        'aspernatur',
    ],
    query='eum',
    refs=[
        shared.TaskRef(
            id='48dc2f61-5199-4ebf-90e9-fe6c632ca3ae',
        ),
    ],
    sort_by=shared.TaskSearchRequestSortBy.TASK_SEARCH_SORT_BY_REVERSE_TICKET_ID,
    subject_ids=[
        'consequatur',
    ],
    task_states=[
        shared.TaskSearchRequestTaskStates.TASK_STATE_UNSPECIFIED,
    ],
    task_types=[
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertifyInput(),
            task_type_grant=shared.TaskTypeGrantInput(
                task_grant_source=shared.TaskGrantSource(
                    external_url='et',
                    integration_id='ducimus',
                ),
            ),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(
                        expired_at=dateutil.parser.isoparse('2021-11-02T19:26:40.219Z'),
                    ),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(
                        expires_at=dateutil.parser.isoparse('2022-10-04T19:57:36.428Z'),
                        last_login=dateutil.parser.isoparse('2022-10-31T07:20:14.068Z'),
                    ),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(
                        request_user_id='doloribus',
                    ),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(
                        access_review_id='nulla',
                        cert_ticket_id='necessitatibus',
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

