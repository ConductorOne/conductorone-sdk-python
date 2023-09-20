# RequestCatalogManagement

### Available Operations

* [add_access_entitlements](#add_access_entitlements) - Add Access Entitlements
* [add_app_entitlements](#add_app_entitlements) - Add App Entitlements
* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - List
* [list_entitlements_for_access](#list_entitlements_for_access) - List Entitlements For Access
* [list_entitlements_per_catalog](#list_entitlements_per_catalog) - List Entitlements Per Catalog
* [remove_access_entitlements](#remove_access_entitlements) - Remove Access Entitlements
* [remove_app_entitlements](#remove_app_entitlements) - Remove App Entitlements
* [update](#update) - Update

## add_access_entitlements

Add visibility bindings (access entitlements) to a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsRequest(
    request_catalog_management_service_add_access_entitlements_request=shared.RequestCatalogManagementServiceAddAccessEntitlementsRequest(
        access_entitlements=[
            shared.AppEntitlementRef(
                app_id='labore',
                id='dbb675fd-5e60-4b37-9ed4-f6fbee41f333',
            ),
        ],
    ),
    catalog_id='beatae',
)

res = s.request_catalog_management.add_access_entitlements(req)

if res.request_catalog_management_service_add_access_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddaccessentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddaccessentitlementsresponse.md)**


## add_app_entitlements

Add requestable entitlements to a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsRequest(
    request_catalog_management_service_add_app_entitlements_request=shared.RequestCatalogManagementServiceAddAppEntitlementsRequest(
        app_entitlements=[
            shared.AppEntitlementRef(
                app_id='dignissimos',
                id='fe35b60e-b1ea-4426-955b-a3c28744ed53',
            ),
        ],
    ),
    catalog_id='cum',
)

res = s.request_catalog_management.add_app_entitlements(req)

if res.request_catalog_management_service_add_app_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                            | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddappentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                           |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddappentitlementsresponse.md)**


## create

Creates a new request catalog.

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

req = shared.RequestCatalogManagementServiceCreateRequest(
    request_catalog_expand_mask=shared.RequestCatalogExpandMask(
        paths=[
            'blanditiis',
        ],
    ),
    description='quas',
    display_name='hic',
    published=False,
    visible_to_everyone=False,
)

res = s.request_catalog_management.create(req)

if res.request_catalog_management_service_get_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [shared.RequestCatalogManagementServiceCreateRequest](../../models/shared/requestcatalogmanagementservicecreaterequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceCreateResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicecreateresponse.md)**


## delete

Delete a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteRequest(
    request_catalog_management_service_delete_request=shared.RequestCatalogManagementServiceDeleteRequest(),
    id='3a8d8f5c-0b2f-42fb-bb19-4a276b26916f',
)

res = s.request_catalog_management.delete(req)

if res.request_catalog_management_service_delete_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeleterequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeleteresponse.md)**


## get

Get a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetRequest(
    id='e1f08f42-94e3-4698-b447-f603e8b445e8',
)

res = s.request_catalog_management.get(req)

if res.request_catalog_management_service_get_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetresponse.md)**


## list

Get a list of request catalogs.

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


res = s.request_catalog_management.list()

if res.request_catalog_management_service_list_response is not None:
    # handle response
```


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistresponse.md)**


## list_entitlements_for_access

List visibility bindings (access entitlements) for a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessRequest(
    catalog_id='sit',
    page_size=7505.95,
    page_token='error',
)

res = s.request_catalog_management.list_entitlements_for_access(req)

if res.request_catalog_management_service_list_entitlements_for_access_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                          | Type                                                                                                                                                                                                               | Required                                                                                                                                                                                                           | Description                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                          | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementsforaccessrequest.md) | :heavy_check_mark:                                                                                                                                                                                                 | The request object to use for the request.                                                                                                                                                                         |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementsforaccessresponse.md)**


## list_entitlements_per_catalog

List entitlements in a catalog that are requestable.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogRequest(
    catalog_id='veniam',
    page_size=3295.43,
    page_token='recusandae',
)

res = s.request_catalog_management.list_entitlements_per_catalog(req)

if res.request_catalog_management_service_list_entitlements_per_catalog_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                            | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementspercatalogrequest.md) | :heavy_check_mark:                                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                                           |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementspercatalogresponse.md)**


## remove_access_entitlements

Remove visibility bindings (access entitlements) to a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsRequest(
    request_catalog_management_service_remove_access_entitlements_request=shared.RequestCatalogManagementServiceRemoveAccessEntitlementsRequest(
        access_entitlements=[
            shared.AppEntitlementRef(
                app_id='reiciendis',
                id='d20e457e-1858-4b6a-89fb-e3a5aa8e4824',
            ),
        ],
    ),
    catalog_id='fugiat',
)

res = s.request_catalog_management.remove_access_entitlements(req)

if res.request_catalog_management_service_remove_access_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                        | Type                                                                                                                                                                                                             | Required                                                                                                                                                                                                         | Description                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                        | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveaccessentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                               | The request object to use for the request.                                                                                                                                                                       |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveaccessentitlementsresponse.md)**


## remove_app_entitlements

Remove requestable entitlements from a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAppEntitlementsRequest(
    request_catalog_management_service_remove_app_entitlements_request=shared.RequestCatalogManagementServiceRemoveAppEntitlementsRequest(
        app_entitlements=[
            shared.AppEntitlementRef(
                app_id='voluptatem',
                id='ab407508-8e51-4862-865e-904f3b1194b8',
            ),
        ],
    ),
    catalog_id='laborum',
)

res = s.request_catalog_management.remove_app_entitlements(req)

if res.request_catalog_management_service_remove_app_entitlements_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAppEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveappentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAppEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveappentitlementsresponse.md)**


## update

Update a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceUpdateRequest(
    request_catalog_management_service_update_request_input=shared.RequestCatalogManagementServiceUpdateRequestInput(
        request_catalog=shared.RequestCatalogInput(
            access_entitlements=[
                shared.AppEntitlementInput(
                    provision_policy=shared.ProvisionPolicy(
                        connector_provision=shared.ConnectorProvision(),
                        delegated_provision=shared.DelegatedProvision(
                            app_id='nam',
                            entitlement_id='tenetur',
                        ),
                        manual_provision=shared.ManualProvision(
                            instructions='laboriosam',
                            user_ids=[
                                'alias',
                            ],
                        ),
                    ),
                    app_id='amet',
                    app_resource_id='deserunt',
                    app_resource_type_id='voluptate',
                    certify_policy_id='unde',
                    compliance_framework_value_ids=[
                        'reiciendis',
                    ],
                    description='provident',
                    display_name='repellendus',
                    duration_grant='delectus',
                    duration_unset=shared.AppEntitlementDurationUnset(),
                    emergency_grant_enabled=False,
                    emergency_grant_policy_id='voluptates',
                    grant_policy_id='perferendis',
                    revoke_policy_id='est',
                    risk_level_value_id='quidem',
                    slug='reprehenderit',
                ),
            ],
            app_ids=[
                'facere',
            ],
            created_by_user_id='fuga',
            description='praesentium',
            display_name='mollitia',
            id='50ce187f-86bc-4173-9689-eee9526f8d98',
            published=False,
            visible_to_everyone=False,
        ),
        request_catalog_expand_mask=shared.RequestCatalogExpandMask(
            paths=[
                'suscipit',
            ],
        ),
        update_mask='repudiandae',
    ),
    id='881ead4f-0e10-4125-a3f9-4e29e973e922',
)

res = s.request_catalog_management.update(req)

if res.request_catalog_management_service_get_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceUpdateRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceupdaterequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceUpdateResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceupdateresponse.md)**

