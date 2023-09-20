# TaskSearch

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
            'repellat',
        ],
    ),
    access_review_ids=[
        'doloribus',
    ],
    account_owner_ids=[
        'ullam',
    ],
    actor_id='in',
    app_entitlement_ids=[
        'nam',
    ],
    app_resource_ids=[
        'earum',
    ],
    app_resource_type_ids=[
        'officia',
    ],
    app_user_subject_ids=[
        'laborum',
    ],
    application_ids=[
        'placeat',
    ],
    assignees_in_ids=[
        'modi',
    ],
    created_after=dateutil.parser.isoparse('2021-04-23T08:23:19.189Z'),
    created_before=dateutil.parser.isoparse('2020-02-18T03:48:05.478Z'),
    current_step=shared.TaskSearchRequestCurrentStep.TASK_SEARCH_CURRENT_STEP_PROVISION,
    emergency_status=shared.TaskSearchRequestEmergencyStatus.UNSPECIFIED,
    exclude_app_entitlement_ids=[
        'rerum',
    ],
    exclude_ids=[
        'tempora',
    ],
    include_deleted=False,
    my_work_user_ids=[
        'quis',
    ],
    opener_ids=[
        'inventore',
    ],
    page_size=1476.85,
    page_token='cumque',
    previously_acted_on_ids=[
        'quae',
    ],
    query='perferendis',
    refs=[
        shared.TaskRef(
            id='32648dc2-f615-4199-abfd-0e9fe6c632ca',
        ),
    ],
    sort_by=shared.TaskSearchRequestSortBy.TASK_SEARCH_SORT_BY_UNSPECIFIED,
    subject_ids=[
        'animi',
    ],
    task_states=[
        shared.TaskSearchRequestTaskStates.TASK_STATE_CLOSED,
    ],
    task_types=[
        shared.TaskTypeInput(
            task_type_certify=shared.TaskTypeCertifyInput(),
            task_type_grant=shared.TaskTypeGrantInput(
                task_grant_source=shared.TaskGrantSource(
                    external_url='nulla',
                    integration_id='consequatur',
                ),
            ),
            task_type_revoke=shared.TaskTypeRevokeInput(
                task_revoke_source=shared.TaskRevokeSource(
                    task_revoke_source_expired=shared.TaskRevokeSourceExpired(
                        expired_at=dateutil.parser.isoparse('2022-11-29T01:33:31.768Z'),
                    ),
                    task_revoke_source_non_usage=shared.TaskRevokeSourceNonUsage(
                        expires_at=dateutil.parser.isoparse('2022-05-19T23:57:30.950Z'),
                        last_login=dateutil.parser.isoparse('2022-03-27T19:38:57.457Z'),
                    ),
                    task_revoke_source_request=shared.TaskRevokeSourceRequest(
                        request_user_id='adipisci',
                    ),
                    task_revoke_source_review=shared.TaskRevokeSourceReview(
                        access_review_id='quasi',
                        cert_ticket_id='magni',
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

