# request_catalog_management

### Available Operations

* [add_access_entitlements](#add_access_entitlements) - Add Access Entitlements
* [add_app_entitlements](#add_app_entitlements) - Add App Entitlements
* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
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
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsRequest(
    request_catalog_management_service_add_access_entitlements_request=shared.RequestCatalogManagementServiceAddAccessEntitlementsRequest(
        access_entitlements=[
            shared.AppEntitlementRef(
                app_id='explicabo',
                id='fb7b194a-276b-4269-96fe-1f08f4294e36',
            ),
            shared.AppEntitlementRef(
                app_id='occaecati',
                id='8f447f60-3e8b-4445-a80c-a55efd20e457',
            ),
            shared.AppEntitlementRef(
                app_id='officiis',
                id='1858b6a8-9fbe-43a5-aa8e-4824d0ab4075',
            ),
            shared.AppEntitlementRef(
                app_id='sit',
                id='88e51862-065e-4904-b3b1-194b8abf603a',
            ),
        ],
    ),
    catalog_id='voluptate',
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
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsRequest(
    request_catalog_management_service_add_app_entitlements_request=shared.RequestCatalogManagementServiceAddAppEntitlementsRequest(
        app_entitlements=[
            shared.AppEntitlementRef(
                app_id='reiciendis',
                id='9dfe0ab7-da8a-450c-a187-f86bc173d689',
            ),
            shared.AppEntitlementRef(
                app_id='officiis',
                id='ee9526f8-d986-4e88-9ead-4f0e1012563f',
            ),
            shared.AppEntitlementRef(
                app_id='molestias',
                id='4e29e973-e922-4a57-a15b-e3e060807e2b',
            ),
        ],
    ),
    catalog_id='iure',
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
        oauth="",
    ),
)

req = shared.RequestCatalogManagementServiceCreateRequest(
    request_catalog_expand_mask=shared.RequestCatalogExpandMask(
        paths=[
            'ratione',
            'laborum',
            'distinctio',
            'voluptatum',
        ],
    ),
    description='rem',
    display_name='aliquam',
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
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteRequest(
    request_catalog_management_service_delete_request=shared.RequestCatalogManagementServiceDeleteRequest(),
    id='5f0597a6-0ff2-4a54-a31e-94764a3e865e',
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
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetRequest(
    id='7956f925-1a5a-49da-a60f-f57bfaad4f9e',
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


## list_entitlements_for_access

List visibility bindings (access entitlements) for a catalog.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessRequest(
    catalog_id='sapiente',
    page_size=7645.62,
    page_token='vitae',
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
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogRequest(
    catalog_id='rerum',
    page_size=2722.29,
    page_token='quis',
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
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsRequest(
    request_catalog_management_service_remove_access_entitlements_request=shared.RequestCatalogManagementServiceRemoveAccessEntitlementsRequest(
        access_entitlements=[
            shared.AppEntitlementRef(
                app_id='fugit',
                id='c1032648-dc2f-4615-999e-bfd0e9fe6c63',
            ),
        ],
    ),
    catalog_id='fugit',
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
        oauth="",
    ),
)

req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAppEntitlementsRequest(
    request_catalog_management_service_remove_app_entitlements_request=shared.RequestCatalogManagementServiceRemoveAppEntitlementsRequest(
        app_entitlements=[
            shared.AppEntitlementRef(
                app_id='fuga',
                id='3aed0117-9963-412f-9e04-771778ff61d0',
            ),
            shared.AppEntitlementRef(
                app_id='dicta',
                id='7476360a-15db-46a6-a065-9a1adeaab585',
            ),
            shared.AppEntitlementRef(
                app_id='vitae',
                id='d6c645b0-8b61-4891-baa0-fe1ade008e6f',
            ),
            shared.AppEntitlementRef(
                app_id='rem',
                id='c5f350d8-cdb5-4a34-9814-3010421813d5',
            ),
        ],
    ),
    catalog_id='consequuntur',
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
                            app_id='quas',
                            entitlement_id='eveniet',
                        ),
                        manual_provision=shared.ManualProvision(
                            instructions='impedit',
                            user_ids=[
                                'esse',
                                'necessitatibus',
                                'sed',
                                'veniam',
                            ],
                        ),
                    ),
                    app_id='nesciunt',
                    app_resource_id='expedita',
                    app_resource_type_id='eum',
                    certify_policy_id='vel',
                    compliance_framework_value_ids=[
                        'magnam',
                        'exercitationem',
                        'ab',
                    ],
                    description='porro',
                    display_name='autem',
                    duration_grant='nobis',
                    duration_unset=shared.AppEntitlementDurationUnset(),
                    emergency_grant_enabled=False,
                    emergency_grant_policy_id='laboriosam',
                    grant_policy_id='recusandae',
                    revoke_policy_id='consequuntur',
                    risk_level_value_id='voluptatem',
                    slug='exercitationem',
                ),
            ],
            app_ids=[
                'quasi',
                'nisi',
                'at',
                'vero',
            ],
            created_by_user_id='est',
            description='harum',
            display_name='sequi',
            id='fec9578a-6458-4427-ba84-18d162309fb0',
            published=False,
            visible_to_everyone=False,
        ),
        request_catalog_expand_mask=shared.RequestCatalogExpandMask(
            paths=[
                'eos',
                'occaecati',
                'iste',
            ],
        ),
        update_mask='magni',
    ),
    id='1aefb9f5-8c4d-486e-a8e4-be056013f59d',
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

