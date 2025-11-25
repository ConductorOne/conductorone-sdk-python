# RequestCatalogManagement
(*request_catalog_management*)

## Overview

### Available Operations

* [add_access_entitlements](#add_access_entitlements) - Add Access Entitlements
* [add_app_entitlements](#add_app_entitlements) - Add App Entitlements
* [create](#create) - Create
* [create_bundle_automation](#create_bundle_automation) - Create Bundle Automation
* [create_requestable_entry](#create_requestable_entry) - Create Requestable Entry
* [delete](#delete) - Delete
* [delete_bundle_automation](#delete_bundle_automation) - Delete Bundle Automation
* [delete_requestable_entry](#delete_requestable_entry) - Delete Requestable Entry
* [force_run_bundle_automation](#force_run_bundle_automation) - Force Run Bundle Automation
* [get](#get) - Get
* [get_bundle_automation](#get_bundle_automation) - Get Bundle Automation
* [get_requestable_entry](#get_requestable_entry) - Get Requestable Entry
* [list](#list) - List
* [list_all_entitlement_ids_per_app](#list_all_entitlement_ids_per_app) - List All Entitlement Ids Per App
* [list_entitlements_for_access](#list_entitlements_for_access) - List Entitlements For Access
* [list_entitlements_per_catalog](#list_entitlements_per_catalog) - List Entitlements Per Catalog
* [remove_access_entitlements](#remove_access_entitlements) - Remove Access Entitlements
* [remove_app_entitlements](#remove_app_entitlements) - Remove App Entitlements
* [resume_paused_bundle_automation](#resume_paused_bundle_automation) - Resume Paused Bundle Automation
* [set_bundle_automation](#set_bundle_automation) - Set Bundle Automation
* [update](#update) - Update
* [update_app_entitlements](#update_app_entitlements) - Update App Entitlements

## add_access_entitlements

Add visibility bindings (access entitlements) to a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.AddAccessEntitlements" method="post" path="/api/v1/catalogs/{catalog_id}/visibility_bindings" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.add_access_entitlements(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_add_access_entitlements_response is not None

    # Handle response
    print(res.request_catalog_management_service_add_access_entitlements_response)

```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddaccessentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                        |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAccessEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddaccessentitlementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## add_app_entitlements

Add requestable entitlements to a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.AddAppEntitlements" method="post" path="/api/v1/catalogs/{catalog_id}/requestable_entries" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.add_app_entitlements(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_add_app_entitlements_response is not None

    # Handle response
    print(res.request_catalog_management_service_add_app_entitlements_response)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                            | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddappentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                           |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceAddAppEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceaddappentitlementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new request catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.Create" method="post" path="/api/v1/catalogs" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.create()

    assert res.request_catalog_management_service_get_response is not None

    # Handle response
    print(res.request_catalog_management_service_get_response)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [shared.RequestCatalogManagementServiceCreateRequest](../../models/shared/requestcatalogmanagementservicecreaterequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceCreateResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicecreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_bundle_automation

Invokes the c1.api.requestcatalog.v1.RequestCatalogManagementService.CreateBundleAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.CreateBundleAutomation" method="post" path="/api/v1/catalogs/{request_catalog_id}/bundle_automation/create" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.create_bundle_automation(request={
        "request_catalog_id": "<id>",
    })

    assert res.bundle_automation is not None

    # Handle response
    print(res.bundle_automation)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceCreateBundleAutomationRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicecreatebundleautomationrequest.md) | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceCreateBundleAutomationResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicecreatebundleautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_requestable_entry

Create a single requestable entry

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.CreateRequestableEntry" method="put" path="/api/v1/catalogs/{catalog_id}/requestable_entries/{app_id}/{entitlement_id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.create_requestable_entry(request={
        "app_id": "<id>",
        "catalog_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.request_catalog_management_service_create_requestable_entry_response is not None

    # Handle response
    print(res.request_catalog_management_service_create_requestable_entry_response)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceCreateRequestableEntryRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicecreaterequestableentryrequest.md) | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceCreateRequestableEntryResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicecreaterequestableentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Delete a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.Delete" method="delete" path="/api/v1/catalogs/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.delete(request={
        "id": "<id>",
    })

    assert res.request_catalog_management_service_delete_response is not None

    # Handle response
    print(res.request_catalog_management_service_delete_response)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeleterequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_bundle_automation

Invokes the c1.api.requestcatalog.v1.RequestCatalogManagementService.DeleteBundleAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.DeleteBundleAutomation" method="delete" path="/api/v1/catalogs/{request_catalog_id}/bundle_automation" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.delete_bundle_automation(request={
        "request_catalog_id": "<id>",
    })

    assert res.delete_bundle_automation_response is not None

    # Handle response
    print(res.delete_bundle_automation_response)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteBundleAutomationRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeletebundleautomationrequest.md) | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteBundleAutomationResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeletebundleautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_requestable_entry

Delete a single requestable entry

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.DeleteRequestableEntry" method="delete" path="/api/v1/catalogs/{catalog_id}/requestable_entries/{app_id}/{entitlement_id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.delete_requestable_entry(request={
        "app_id": "<id>",
        "catalog_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.request_catalog_management_service_delete_requestable_entry_response is not None

    # Handle response
    print(res.request_catalog_management_service_delete_requestable_entry_response)

```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteRequestableEntryRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeleterequestableentryrequest.md) | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                          |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceDeleteRequestableEntryResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicedeleterequestableentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## force_run_bundle_automation

Invokes the c1.api.requestcatalog.v1.RequestCatalogManagementService.ForceRunBundleAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.ForceRunBundleAutomation" method="post" path="/api/v1/catalogs/{request_catalog_id}/bundle_automation/run" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.force_run_bundle_automation(request={
        "request_catalog_id": "<id>",
    })

    assert res.force_run_bundle_automation_response is not None

    # Handle response
    print(res.force_run_bundle_automation_response)

```

### Parameters

| Parameter                                                                                                                                                                                                        | Type                                                                                                                                                                                                             | Required                                                                                                                                                                                                         | Description                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                        | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceForceRunBundleAutomationRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceforcerunbundleautomationrequest.md) | :heavy_check_mark:                                                                                                                                                                                               | The request object to use for the request.                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                              |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceForceRunBundleAutomationResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceforcerunbundleautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Get a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.Get" method="get" path="/api/v1/catalogs/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.get(request={
        "id": "<id>",
    })

    assert res.request_catalog_management_service_get_response is not None

    # Handle response
    print(res.request_catalog_management_service_get_response)

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |
| `retries`                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                    |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_bundle_automation

Get bundle automation

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.GetBundleAutomation" method="get" path="/api/v1/catalogs/{request_catalog_id}/bundle_automation" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.get_bundle_automation(request={
        "request_catalog_id": "<id>",
    })

    assert res.bundle_automation is not None

    # Handle response
    print(res.bundle_automation)

```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                              | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetBundleAutomationRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetbundleautomationrequest.md) | :heavy_check_mark:                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                             |
| `retries`                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                    |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetBundleAutomationResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetbundleautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_requestable_entry

Get a single requestable entry

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.GetRequestableEntry" method="get" path="/api/v1/catalogs/{catalog_id}/requestable_entries/{app_id}/{entitlement_id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.get_requestable_entry(request={
        "app_id": "<id>",
        "catalog_id": "<id>",
        "entitlement_id": "<id>",
    })

    assert res.request_catalog_management_service_get_requestable_entry_response is not None

    # Handle response
    print(res.request_catalog_management_service_get_requestable_entry_response)

```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                              | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetRequestableEntryRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetrequestableentryrequest.md) | :heavy_check_mark:                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                             |
| `retries`                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                    |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceGetRequestableEntryResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicegetrequestableentryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

Get a list of request catalogs.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.List" method="get" path="/api/v1/catalogs" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.list()

    assert res.request_catalog_management_service_list_response is not None

    # Handle response
    print(res.request_catalog_management_service_list_response)

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistrequest.md) | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_all_entitlement_ids_per_app

Invokes the c1.api.requestcatalog.v1.RequestCatalogManagementService.ListAllEntitlementIdsPerApp method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.ListAllEntitlementIdsPerApp" method="get" path="/api/v1/catalogs/{catalog_id}/requestable_entitlementIDs" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.list_all_entitlement_ids_per_app(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_list_all_entitlement_ids_per_catalog_response is not None

    # Handle response
    print(res.request_catalog_management_service_list_all_entitlement_ids_per_catalog_response)

```

### Parameters

| Parameter                                                                                                                                                                                                              | Type                                                                                                                                                                                                                   | Required                                                                                                                                                                                                               | Description                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                              | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListAllEntitlementIdsPerAppRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistallentitlementidsperapprequest.md) | :heavy_check_mark:                                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                    |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListAllEntitlementIdsPerAppResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistallentitlementidsperappresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_entitlements_for_access

List visibility bindings (access entitlements) for a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.ListEntitlementsForAccess" method="get" path="/api/v1/catalogs/{catalog_id}/visibility_entitlements" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.list_entitlements_for_access(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_list_entitlements_for_access_response is not None

    # Handle response
    print(res.request_catalog_management_service_list_entitlements_for_access_response)

```

### Parameters

| Parameter                                                                                                                                                                                                          | Type                                                                                                                                                                                                               | Required                                                                                                                                                                                                           | Description                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                          | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementsforaccessrequest.md) | :heavy_check_mark:                                                                                                                                                                                                 | The request object to use for the request.                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                                                |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsForAccessResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementsforaccessresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_entitlements_per_catalog

List entitlements in a catalog that are requestable.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.ListEntitlementsPerCatalog" method="get" path="/api/v1/catalogs/{catalog_id}/requestable_entitlements" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.list_entitlements_per_catalog(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_list_entitlements_per_catalog_response is not None

    # Handle response
    print(res.request_catalog_management_service_list_entitlements_per_catalog_response)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                            | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementspercatalogrequest.md) | :heavy_check_mark:                                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListEntitlementsPerCatalogResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicelistentitlementspercatalogresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_access_entitlements

Remove visibility bindings (access entitlements) to a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.RemoveAccessEntitlements" method="delete" path="/api/v1/catalogs/{catalog_id}/visibility_bindings" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.remove_access_entitlements(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_remove_access_entitlements_response is not None

    # Handle response
    print(res.request_catalog_management_service_remove_access_entitlements_response)

```

### Parameters

| Parameter                                                                                                                                                                                                        | Type                                                                                                                                                                                                             | Required                                                                                                                                                                                                         | Description                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                        | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveaccessentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                               | The request object to use for the request.                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                              |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAccessEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveaccessentitlementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## remove_app_entitlements

Remove requestable entitlements from a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.RemoveAppEntitlements" method="delete" path="/api/v1/catalogs/{catalog_id}/requestable_entries" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.remove_app_entitlements(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_remove_app_entitlements_response is not None

    # Handle response
    print(res.request_catalog_management_service_remove_app_entitlements_response)

```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAppEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveappentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                        |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceRemoveAppEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceremoveappentitlementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## resume_paused_bundle_automation

Invokes the c1.api.requestcatalog.v1.RequestCatalogManagementService.ResumePausedBundleAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.ResumePausedBundleAutomation" method="post" path="/api/v1/catalogs/{request_catalog_id}/bundle_automation/resume" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.resume_paused_bundle_automation(request={
        "request_catalog_id": "<id>",
    })

    assert res.resume_paused_bundle_automation_response is not None

    # Handle response
    print(res.resume_paused_bundle_automation_response)

```

### Parameters

| Parameter                                                                                                                                                                                                                | Type                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                 | Description                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceResumePausedBundleAutomationRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceresumepausedbundleautomationrequest.md) | :heavy_check_mark:                                                                                                                                                                                                       | The request object to use for the request.                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                      |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceResumePausedBundleAutomationResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceresumepausedbundleautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## set_bundle_automation

Invokes the c1.api.requestcatalog.v1.RequestCatalogManagementService.SetBundleAutomation method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.SetBundleAutomation" method="post" path="/api/v1/catalogs/{request_catalog_id}/bundle_automation" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.set_bundle_automation(request={
        "request_catalog_id": "<id>",
    })

    assert res.bundle_automation is not None

    # Handle response
    print(res.bundle_automation)

```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                              | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceSetBundleAutomationRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicesetbundleautomationrequest.md) | :heavy_check_mark:                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                             |
| `retries`                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                    |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceSetBundleAutomationResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementservicesetbundleautomationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update a catalog.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.Update" method="post" path="/api/v1/catalogs/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.update(request={
        "id": "<id>",
    })

    assert res.request_catalog_management_service_get_response is not None

    # Handle response
    print(res.request_catalog_management_service_get_response)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceUpdateRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceupdaterequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceUpdateResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_app_entitlements

Invokes the c1.api.requestcatalog.v1.RequestCatalogManagementService.UpdateAppEntitlements method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.requestcatalog.v1.RequestCatalogManagementService.UpdateAppEntitlements" method="post" path="/api/v1/catalogs/{catalog_id}/requestable_entitlements/update" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.request_catalog_management.update_app_entitlements(request={
        "catalog_id": "<id>",
    })

    assert res.request_catalog_management_service_update_app_entitlements_response is not None

    # Handle response
    print(res.request_catalog_management_service_update_app_entitlements_response)

```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.C1APIRequestcatalogV1RequestCatalogManagementServiceUpdateAppEntitlementsRequest](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceupdateappentitlementsrequest.md) | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                        |

### Response

**[operations.C1APIRequestcatalogV1RequestCatalogManagementServiceUpdateAppEntitlementsResponse](../../models/operations/c1apirequestcatalogv1requestcatalogmanagementserviceupdateappentitlementsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |