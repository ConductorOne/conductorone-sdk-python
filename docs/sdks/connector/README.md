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
                'saepe',
            ],
        ),
        catalog_id='suscipit',
        config={
            "deserunt": 'provident',
        },
        description='minima',
        user_ids=[
            'repellendus',
        ],
    ),
    app_id='totam',
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
                'similique',
            ],
        ),
        catalog_id='alias',
        description='at',
        display_name='quaerat',
        user_ids=[
            'tempora',
        ],
    ),
    app_id='vel',
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
    app_id='quod',
    id='e2af7a73-cf3b-4e45-bf87-0b326b5a7342',
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
    app_id='cupiditate',
    id='cdb1a842-2bb6-479d-a322-715bf0cbb1e3',
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
    app_id='veritatis',
    connector_id='nobis',
    id='8b90f344-3a11-408e-8adc-f4b921879fce',
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
    app_id='omnis',
    page_size=3381.59,
    page_token='ipsum',
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
    app_id='delectus',
    connector_id='voluptate',
    id='3ef7fbc7-abd7-44dd-b9c0-f5d2cff7c70a',
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
    app_id='tempora',
    connector_id='ipsam',
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
                completed_at=dateutil.parser.isoparse('2022-11-12T00:45:12.094Z'),
                last_error='vel',
                started_at=dateutil.parser.isoparse('2022-02-08T20:43:00.221Z'),
                status=shared.ConnectorStatusStatus.SYNC_STATUS_UNSPECIFIED,
                updated_at=dateutil.parser.isoparse('2022-06-28T08:50:44.084Z'),
            ),
            o_auth2_authorized_as=shared.OAuth2AuthorizedAsInput(),
            app_id='dicta',
            config={
                "dolor": 'maiores',
            },
            description='quasi',
            display_name='ex',
            id='d9f5fce6-c556-4146-83e2-50fb008c42e1',
            user_ids=[
                'non',
            ],
        ),
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'et',
            ],
        ),
        update_mask='dolorum',
    ),
    app_id='laborum',
    id='c366c8dd-6b14-4429-8747-4778a7bd466d',
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
                completed_at=dateutil.parser.isoparse('2022-06-29T02:09:48.123Z'),
                last_error='quisquam',
                started_at=dateutil.parser.isoparse('2022-12-11T06:00:38.230Z'),
                status=shared.ConnectorStatusStatus.SYNC_STATUS_DONE,
                updated_at=dateutil.parser.isoparse('2022-08-03T04:27:44.236Z'),
            ),
            o_auth2_authorized_as=shared.OAuth2AuthorizedAsInput(),
            app_id='quo',
            config={
                "illum": 'quo',
            },
            description='fuga',
            display_name='eius',
            id='251904e5-23c7-4e0b-8717-8e4796f2a70c',
            user_ids=[
                'eum',
            ],
        ),
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'quas',
            ],
        ),
        update_mask='praesentium',
    ),
    connector_app_id='consequuntur',
    connector_id='deleniti',
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

