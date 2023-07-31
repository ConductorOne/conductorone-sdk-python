<!-- Start SDK Example Usage -->


```python
import sdk
from sdk.models import shared

s = sdk.SDKWithCredentials("CLIENT_ID", "CLIENT_SECRET")

req = shared.AppEntitlementSearchServiceSearchRequest(
    app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
        paths=[
            'provident',
            'distinctio',
            'quibusdam',
        ],
    ),
    access_review_id='unde',
    alias='nulla',
    app_ids=[
        'illum',
        'vel',
        'error',
    ],
    app_user_ids=[
        'suscipit',
        'iure',
        'magnam',
    ],
    compliance_framework_ids=[
        'ipsa',
        'delectus',
        'tempora',
        'suscipit',
    ],
    exclude_app_ids=[
        'minus',
        'placeat',
    ],
    exclude_app_user_ids=[
        'iusto',
        'excepturi',
        'nisi',
    ],
    only_get_expiring=False,
    page_size=9255.97,
    page_token='temporibus',
    query='ab',
    resource_type_ids=[
        'veritatis',
        'deserunt',
    ],
    risk_level_ids=[
        'ipsam',
    ],
)

res = s.app_entitlement_search.search(req)

if res.app_entitlement_search_service_search_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->