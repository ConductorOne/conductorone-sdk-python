# connector

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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceCreateRequest(
    connector_service_create_request=shared.ConnectorServiceCreateRequest(
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'saepe',
                'eius',
                'aspernatur',
            ],
        ),
        catalog_id='perferendis',
        config={
            "optio": 'accusamus',
        },
        description='ad',
        user_ids=[
            'suscipit',
            'deserunt',
            'provident',
            'minima',
        ],
    ),
    app_id='repellendus',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceCreateDelegatedRequest(
    connector_service_create_delegated_request=shared.ConnectorServiceCreateDelegatedRequest(
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'similique',
                'alias',
                'at',
            ],
        ),
        catalog_id='quaerat',
        description='tempora',
        display_name='vel',
        user_ids=[
            'officiis',
            'qui',
            'dolorum',
            'a',
        ],
    ),
    app_id='esse',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceDeleteRequest(
    connector_service_delete_request=shared.ConnectorServiceDeleteRequest(),
    app_id='harum',
    id='73cf3be4-53f8-470b-b26b-5a73429cdb1a',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceGetRequest(
    app_id='totam',
    id='422bb679-d232-4271-9bf0-cbb1e31b8b90',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceGetCredentialsRequest(
    app_id='delectus',
    connector_id='dolorem',
    id='443a1108-e0ad-4cf4-b921-879fce953f73',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceListRequest(
    app_id='vero',
    page_size=9493.19,
    page_token='dignissimos',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceRevokeCredentialRequest(
    connector_service_revoke_credential_request=shared.ConnectorServiceRevokeCredentialRequest(),
    app_id='hic',
    connector_id='distinctio',
    id='c7abd74d-d39c-40f5-92cf-f7c70a45626d',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceRotateCredentialRequest(
    connector_service_rotate_credential_request=shared.ConnectorServiceRotateCredentialRequest(),
    app_id='magnam',
    connector_id='ratione',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceUpdateRequest(
    connector_service_update_request_input=shared.ConnectorServiceUpdateRequestInput(
        connector=shared.ConnectorInput(
            connector_status=shared.ConnectorStatus(
                completed_at=dateutil.parser.isoparse('2022-06-28T08:50:44.084Z'),
                last_error='dicta',
                started_at=dateutil.parser.isoparse('2022-01-08T01:04:15.076Z'),
                status=shared.ConnectorStatusStatus.SYNC_STATUS_UNSPECIFIED,
                updated_at=dateutil.parser.isoparse('2022-02-20T07:12:08.273Z'),
            ),
            o_auth2_authorized_as=shared.OAuth2AuthorizedAs1(),
            app_id='excepturi',
            config={
                "nostrum": 'sapiente',
                "quisquam": 'saepe',
                "ea": 'impedit',
                "corporis": 'veniam',
            },
            description='aliquid',
            display_name='inventore',
            id='46c3e250-fb00-48c4-ae14-1aac366c8dd6',
            user_ids=[
                'quasi',
                'tempora',
                'numquam',
            ],
        ),
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'provident',
            ],
        ),
        update_mask='ipsa',
    ),
    app_id='molestiae',
    id='474778a7-bd46-46d2-8c10-ab3cdca42519',
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
        oauth="",
    ),
)

req = operations.C1APIAppV1ConnectorServiceUpdateDelegatedRequest(
    connector_service_update_delegated_request_input=shared.ConnectorServiceUpdateDelegatedRequestInput(
        connector=shared.ConnectorInput(
            connector_status=shared.ConnectorStatus(
                completed_at=dateutil.parser.isoparse('2022-09-23T10:04:47.931Z'),
                last_error='debitis',
                started_at=dateutil.parser.isoparse('2022-11-13T06:50:40.250Z'),
                status=shared.ConnectorStatusStatus.SYNC_STATUS_UNSPECIFIED,
                updated_at=dateutil.parser.isoparse('2021-08-15T10:59:14.485Z'),
            ),
            o_auth2_authorized_as=shared.OAuth2AuthorizedAs1(),
            app_id='recusandae',
            config={
                "distinctio": 'quod',
            },
            description='dignissimos',
            display_name='inventore',
            id='78e4796f-2a70-4c68-8282-aa482562f222',
            user_ids=[
                'occaecati',
                'atque',
                'et',
                'esse',
            ],
        ),
        connector_expand_mask=shared.ConnectorExpandMask(
            paths=[
                'accusamus',
                'veritatis',
                'esse',
                'quod',
            ],
        ),
        update_mask='nam',
    ),
    connector_app_id='vero',
    connector_id='aliquid',
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

