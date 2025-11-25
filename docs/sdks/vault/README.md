# Vault
(*vault*)

## Overview

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [update](#update) - Update

## create

Invokes the c1.api.vault.v1.VaultService.Create method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.vault.v1.VaultService.Create" method="post" path="/api/v1/vaults" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.vault.create(request={
        "display_name": "Nola.Fahey",
    })

    assert res.vault_service_create_response is not None

    # Handle response
    print(res.vault_service_create_response)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.VaultServiceCreateRequest](../../models/shared/vaultservicecreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.C1APIVaultV1VaultServiceCreateResponse](../../models/operations/c1apivaultv1vaultservicecreateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete

Invokes the c1.api.vault.v1.VaultService.Delete method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.vault.v1.VaultService.Delete" method="delete" path="/api/v1/vaults/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.vault.delete(request={
        "vault_service_delete_request": {},
        "id": "<id>",
    })

    assert res.vault_service_delete_response is not None

    # Handle response
    print(res.vault_service_delete_response)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIVaultV1VaultServiceDeleteRequest](../../models/operations/c1apivaultv1vaultservicedeleterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.C1APIVaultV1VaultServiceDeleteResponse](../../models/operations/c1apivaultv1vaultservicedeleteresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Invokes the c1.api.vault.v1.VaultService.Get method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.vault.v1.VaultService.Get" method="get" path="/api/v1/vaults/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.vault.get(request={
        "id": "<id>",
    })

    assert res.vault_service_get_response is not None

    # Handle response
    print(res.vault_service_get_response)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.C1APIVaultV1VaultServiceGetRequest](../../models/operations/c1apivaultv1vaultservicegetrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.C1APIVaultV1VaultServiceGetResponse](../../models/operations/c1apivaultv1vaultservicegetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.vault.v1.VaultService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.vault.v1.VaultService.Update" method="post" path="/api/v1/vaults/{id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.vault.update(request={
        "vault_service_update_request": {},
        "id": "<id>",
    })

    assert res.vault_service_update_response is not None

    # Handle response
    print(res.vault_service_update_response)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIVaultV1VaultServiceUpdateRequest](../../models/operations/c1apivaultv1vaultserviceupdaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[operations.C1APIVaultV1VaultServiceUpdateResponse](../../models/operations/c1apivaultv1vaultserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |