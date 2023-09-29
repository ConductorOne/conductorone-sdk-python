# RequestCatalogManagement
(*request_catalog_management*)

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
                app_id='deposit',
                id='<ID>',
            ),
        ],
    ),
    catalog_id='Principal',
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
                app_id='East cyan Wilma',
                id='<ID>',
            ),
        ],
    ),
    catalog_id='Southeast Steel slight',
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
            'neural',
        ],
    ),
    description='Expanded zero tolerance migration',
    display_name='Sausages ASCII',
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
    id='<ID>',
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
    id='<ID>',
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
    catalog_id='mint digital Man',
    page_size=4915.05,
    page_token='sympathetically',
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
    catalog_id='Senior',
    page_size=7955.89,
    page_token='male',
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
                app_id='Mill Audi indigo',
                id='<ID>',
            ),
        ],
    ),
    catalog_id='Director',
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
                app_id='UTF8',
                id='<ID>',
            ),
        ],
    ),
    catalog_id='bus',
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
                            app_id='South complexity',
                            entitlement_id='Tempe Ruble ADP',
                        ),
                        manual_provision=shared.ManualProvision(
                            instructions='Holmium',
                            user_ids=[
                                'Country',
                            ],
                        ),
                    ),
                    app_id='Albany Southeast Computer',
                    app_resource_id='Towels',
                    app_resource_type_id='invoice Northeast orange',
                    certify_policy_id='Response HTTP',
                    compliance_framework_value_ids=[
                        'Hybrid',
                    ],
                    description='Stand-alone encompassing middleware',
                    display_name='index Iran after',
                    duration_grant='through',
                    duration_unset=shared.AppEntitlementDurationUnset(),
                    emergency_grant_enabled=False,
                    emergency_grant_policy_id='Optimized',
                    grant_policy_id='fugit fuchsia',
                    revoke_policy_id='sternly meter experiences',
                    risk_level_value_id='as Electric than',
                    slug='Benz Representative',
                ),
            ],
            app_ids=[
                'wireless',
            ],
            created_by_user_id='index',
            description='Public-key methodical info-mediaries',
            display_name='Virgin',
            id='<ID>',
            published=False,
            visible_to_everyone=False,
        ),
        request_catalog_expand_mask=shared.RequestCatalogExpandMask(
            paths=[
                'relationships',
            ],
        ),
        update_mask='Northeast Executive',
    ),
    id='<ID>',
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

