# Connector
(*connector*)

### Available Operations

* [create](#create) - Create
* [create_delegated](#create_delegated) - Create Delegated
* [delete](#delete) - Delete
* [force_sync](#force_sync) - Force Sync
* [get](#get) - Get
* [get_credentials](#get_credentials) - Get Credentials
* [list](#list) - List
* [revoke_credential](#revoke_credential) - Revoke Credential
* [rotate_credential](#rotate_credential) - Rotate Credential
* [update](#update) - Update
* [update_delegated](#update_delegated) - Update Delegated

## create

Create a configured connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceCreateRequest(
    app_id='<value>',
)

res = s.connector.create(req)

if res.connector_service_create_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1ConnectorServiceCreateRequest](../../models/operations/c1apiappv1connectorservicecreaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceCreateResponse](../../models/operations/c1apiappv1connectorservicecreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_delegated

Create a connector that is pending a connector config.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceCreateDelegatedRequest(
    app_id='<value>',
)

res = s.connector.create_delegated(req)

if res.connector_service_create_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIAppV1ConnectorServiceCreateDelegatedRequest](../../models/operations/c1apiappv1connectorservicecreatedelegatedrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.C1APIAppV1ConnectorServiceCreateDelegatedResponse](../../models/operations/c1apiappv1connectorservicecreatedelegatedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete a connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceDeleteRequest(
    app_id='<value>',
    id='<id>',
)

res = s.connector.delete(req)

if res.connector_service_delete_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1ConnectorServiceDeleteRequest](../../models/operations/c1apiappv1connectorservicedeleterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceDeleteResponse](../../models/operations/c1apiappv1connectorservicedeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## force_sync

Invokes the c1.api.app.v1.ConnectorService.ForceSync method.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceForceSyncRequest(
    app_id='<value>',
    connector_id='<value>',
)

res = s.connector.force_sync(req)

if res.force_sync_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.C1APIAppV1ConnectorServiceForceSyncRequest](../../models/operations/c1apiappv1connectorserviceforcesyncrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.C1APIAppV1ConnectorServiceForceSyncResponse](../../models/operations/c1apiappv1connectorserviceforcesyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get a connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceGetRequest(
    app_id='<value>',
    id='<id>',
)

res = s.connector.get(req)

if res.connector_service_get_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.C1APIAppV1ConnectorServiceGetRequest](../../models/operations/c1apiappv1connectorservicegetrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.C1APIAppV1ConnectorServiceGetResponse](../../models/operations/c1apiappv1connectorservicegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_credentials

Get credentials for a connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceGetCredentialsRequest(
    app_id='<value>',
    connector_id='<value>',
    id='<id>',
)

res = s.connector.get_credentials(req)

if res.connector_service_get_credentials_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.C1APIAppV1ConnectorServiceGetCredentialsRequest](../../models/operations/c1apiappv1connectorservicegetcredentialsrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceGetCredentialsResponse](../../models/operations/c1apiappv1connectorservicegetcredentialsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list

List connectors for an app.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceListRequest(
    app_id='<value>',
)

res = s.connector.list(req)

if res.connector_service_list_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1ConnectorServiceListRequest](../../models/operations/c1apiappv1connectorservicelistrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.C1APIAppV1ConnectorServiceListResponse](../../models/operations/c1apiappv1connectorservicelistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## revoke_credential

Revoke credentials for a connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceRevokeCredentialRequest(
    app_id='<value>',
    connector_id='<value>',
    id='<id>',
)

res = s.connector.revoke_credential(req)

if res.connector_service_revoke_credential_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.C1APIAppV1ConnectorServiceRevokeCredentialRequest](../../models/operations/c1apiappv1connectorservicerevokecredentialrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.C1APIAppV1ConnectorServiceRevokeCredentialResponse](../../models/operations/c1apiappv1connectorservicerevokecredentialresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## rotate_credential

Rotate credentials for a connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceRotateCredentialRequest(
    app_id='<value>',
    connector_id='<value>',
)

res = s.connector.rotate_credential(req)

if res.connector_service_rotate_credential_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.C1APIAppV1ConnectorServiceRotateCredentialRequest](../../models/operations/c1apiappv1connectorservicerotatecredentialrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.C1APIAppV1ConnectorServiceRotateCredentialResponse](../../models/operations/c1apiappv1connectorservicerotatecredentialresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceUpdateRequest(
    app_id='<value>',
    id='<id>',
)

res = s.connector.update(req)

if res.connector_service_update_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1ConnectorServiceUpdateRequest](../../models/operations/c1apiappv1connectorserviceupdaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceUpdateResponse](../../models/operations/c1apiappv1connectorserviceupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_delegated

Update a delegated connector.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
    ),
)

req = operations.C1APIAppV1ConnectorServiceUpdateDelegatedRequest(
    connector_app_id='<value>',
    connector_id='<value>',
)

res = s.connector.update_delegated(req)

if res.connector_service_update_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIAppV1ConnectorServiceUpdateDelegatedRequest](../../models/operations/c1apiappv1connectorserviceupdatedelegatedrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.C1APIAppV1ConnectorServiceUpdateDelegatedResponse](../../models/operations/c1apiappv1connectorserviceupdatedelegatedresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
