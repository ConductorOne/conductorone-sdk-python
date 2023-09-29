# Connector
(*connector*)

### Available Operations

* [create](#create) - Create
* [create_delegated](#create_delegated) - Create Delegated
* [delete](#delete) - Delete
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
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceCreateRequest(
    connector_service_create_request=shared.ConnectorServiceCreateRequest(
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'neural',
            ],
        ),
        catalog_id='pirouette',
        config={
            "laboriosam": 'Sausages',
        },
        description='Multi-layered background pricing structure',
        user_ids=[
            'alarm',
        ],
    ),
    app_id='Lauderhill connecting',
)

res = s.connector.create(req)

if res.connector_service_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1ConnectorServiceCreateRequest](../../models/operations/c1apiappv1connectorservicecreaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceCreateResponse](../../models/operations/c1apiappv1connectorservicecreateresponse.md)**


## create_delegated

Create a connector that is pending a connector config.

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

req = operations.C1APIAppV1ConnectorServiceCreateDelegatedRequest(
    connector_service_create_delegated_request=shared.ConnectorServiceCreateDelegatedRequest(
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'Keyboard',
            ],
        ),
        catalog_id='obtrude',
        description='Face to face tangible superstructure',
        display_name='female',
        user_ids=[
            'Tools',
        ],
    ),
    app_id='Land Rock',
)

res = s.connector.create_delegated(req)

if res.connector_service_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIAppV1ConnectorServiceCreateDelegatedRequest](../../models/operations/c1apiappv1connectorservicecreatedelegatedrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.C1APIAppV1ConnectorServiceCreateDelegatedResponse](../../models/operations/c1apiappv1connectorservicecreatedelegatedresponse.md)**


## delete

Delete a connector.

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

req = operations.C1APIAppV1ConnectorServiceDeleteRequest(
    connector_service_delete_request=shared.ConnectorServiceDeleteRequest(),
    app_id='Architect Cotton port',
    id='<ID>',
)

res = s.connector.delete(req)

if res.connector_service_delete_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1ConnectorServiceDeleteRequest](../../models/operations/c1apiappv1connectorservicedeleterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceDeleteResponse](../../models/operations/c1apiappv1connectorservicedeleteresponse.md)**


## get

Get a connector.

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

req = operations.C1APIAppV1ConnectorServiceGetRequest(
    app_id='Group Cambridgeshire',
    id='<ID>',
)

res = s.connector.get(req)

if res.connector_service_get_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.C1APIAppV1ConnectorServiceGetRequest](../../models/operations/c1apiappv1connectorservicegetrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.C1APIAppV1ConnectorServiceGetResponse](../../models/operations/c1apiappv1connectorservicegetresponse.md)**


## get_credentials

Get credentials for a connector.

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

req = operations.C1APIAppV1ConnectorServiceGetCredentialsRequest(
    app_id='reluctance',
    connector_id='Cambridgeshire',
    id='<ID>',
)

res = s.connector.get_credentials(req)

if res.connector_service_get_credentials_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.C1APIAppV1ConnectorServiceGetCredentialsRequest](../../models/operations/c1apiappv1connectorservicegetcredentialsrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceGetCredentialsResponse](../../models/operations/c1apiappv1connectorservicegetcredentialsresponse.md)**


## list

List connectors for an app.

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

req = operations.C1APIAppV1ConnectorServiceListRequest(
    app_id='Bronze Architect',
    page_size=9628.76,
    page_token='female',
)

res = s.connector.list(req)

if res.connector_service_list_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.C1APIAppV1ConnectorServiceListRequest](../../models/operations/c1apiappv1connectorservicelistrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.C1APIAppV1ConnectorServiceListResponse](../../models/operations/c1apiappv1connectorservicelistresponse.md)**


## revoke_credential

Revoke credentials for a connector.

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

req = operations.C1APIAppV1ConnectorServiceRevokeCredentialRequest(
    connector_service_revoke_credential_request=shared.ConnectorServiceRevokeCredentialRequest(),
    app_id='Supervisor Senior',
    connector_id='North as symbolise',
    id='<ID>',
)

res = s.connector.revoke_credential(req)

if res.connector_service_revoke_credential_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.C1APIAppV1ConnectorServiceRevokeCredentialRequest](../../models/operations/c1apiappv1connectorservicerevokecredentialrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.C1APIAppV1ConnectorServiceRevokeCredentialResponse](../../models/operations/c1apiappv1connectorservicerevokecredentialresponse.md)**


## rotate_credential

Rotate credentials for a connector.

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

req = operations.C1APIAppV1ConnectorServiceRotateCredentialRequest(
    connector_service_rotate_credential_request=shared.ConnectorServiceRotateCredentialRequest(),
    app_id='yawningly Clothing',
    connector_id='watt functional ferociously',
)

res = s.connector.rotate_credential(req)

if res.connector_service_rotate_credential_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.C1APIAppV1ConnectorServiceRotateCredentialRequest](../../models/operations/c1apiappv1connectorservicerotatecredentialrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.C1APIAppV1ConnectorServiceRotateCredentialResponse](../../models/operations/c1apiappv1connectorservicerotatecredentialresponse.md)**


## update

Update a connector.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceUpdateRequest(
    connector_service_update_request_input=shared.ConnectorServiceUpdateRequestInput(
        connector=shared.ConnectorInput(
            connector_status=shared.ConnectorStatus(
                completed_at=dateutil.parser.isoparse('2022-08-25T07:18:46.400Z'),
                last_error='Gender',
                started_at=dateutil.parser.isoparse('2023-01-24T19:54:18.196Z'),
                status=shared.ConnectorStatusStatus.SYNC_STATUS_UNSPECIFIED,
                updated_at=dateutil.parser.isoparse('2023-08-31T09:59:08.279Z'),
            ),
            o_auth2_authorized_as=shared.OAuth2AuthorizedAsInput(),
            app_id='Ohio ADP',
            config={
                "dicta": 'Holmium',
            },
            description='Grass-roots secondary matrices',
            display_name='alarmed North',
            id='<ID>',
            user_ids=[
                'Chevrolet',
            ],
        ),
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'Northeast',
            ],
        ),
        update_mask='laborum',
    ),
    app_id='capitalize mint',
    id='<ID>',
)

res = s.connector.update(req)

if res.connector_service_update_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.C1APIAppV1ConnectorServiceUpdateRequest](../../models/operations/c1apiappv1connectorserviceupdaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.C1APIAppV1ConnectorServiceUpdateResponse](../../models/operations/c1apiappv1connectorserviceupdateresponse.md)**


## update_delegated

Update a delegated connector.

### Example Usage

```python
import sdk
import dateutil.parser
from sdk.models import operations, shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceUpdateDelegatedRequest(
    connector_service_update_delegated_request_input=shared.ConnectorServiceUpdateDelegatedRequestInput(
        connector=shared.ConnectorInput(
            connector_status=shared.ConnectorStatus(
                completed_at=dateutil.parser.isoparse('2022-10-12T21:45:05.114Z'),
                last_error='Ouguiya methodologies North',
                started_at=dateutil.parser.isoparse('2022-04-11T03:27:06.440Z'),
                status=shared.ConnectorStatusStatus.SYNC_STATUS_DONE,
                updated_at=dateutil.parser.isoparse('2023-11-25T06:25:11.398Z'),
            ),
            o_auth2_authorized_as=shared.OAuth2AuthorizedAsInput(),
            app_id='support since Director',
            config={
                "consequuntur": 'instead',
            },
            description='Advanced leading edge superstructure',
            display_name='aut',
            id='<ID>',
            user_ids=[
                'upon',
            ],
        ),
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'Wooden',
            ],
        ),
        update_mask='er Southeast',
    ),
    connector_app_id='invoice Account',
    connector_id='except ASCII driver',
)

res = s.connector.update_delegated(req)

if res.connector_service_update_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.C1APIAppV1ConnectorServiceUpdateDelegatedRequest](../../models/operations/c1apiappv1connectorserviceupdatedelegatedrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.C1APIAppV1ConnectorServiceUpdateDelegatedResponse](../../models/operations/c1apiappv1connectorserviceupdatedelegatedresponse.md)**

