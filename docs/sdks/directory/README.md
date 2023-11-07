# Directory
(*.directory*)

### Available Operations

* [create](#create) - Create
* [delete](#delete) - Delete
* [get](#get) - Get
* [list](#list) - List

## create

Create a directory.

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

req = shared.DirectoryServiceCreateRequest(
    directory_expand_mask=shared.DirectoryExpandMask(
        paths=[
            'string',
        ],
    ),
)

res = s.directory.create(req)

if res.directory_service_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.DirectoryServiceCreateRequest](../../models/shared/directoryservicecreaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.C1APIDirectoryV1DirectoryServiceCreateResponse](../../models/operations/c1apidirectoryv1directoryservicecreateresponse.md)**


## delete

Delete a directory by app_id.

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

req = operations.C1APIDirectoryV1DirectoryServiceDeleteRequest(
    directory_service_delete_request=shared.DirectoryServiceDeleteRequest(),
    app_id='string',
)

res = s.directory.delete(req)

if res.directory_service_delete_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.C1APIDirectoryV1DirectoryServiceDeleteRequest](../../models/operations/c1apidirectoryv1directoryservicedeleterequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.C1APIDirectoryV1DirectoryServiceDeleteResponse](../../models/operations/c1apidirectoryv1directoryservicedeleteresponse.md)**


## get

Get a directory by app_id.

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

req = operations.C1APIDirectoryV1DirectoryServiceGetRequest(
    app_id='string',
)

res = s.directory.get(req)

if res.directory_service_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.C1APIDirectoryV1DirectoryServiceGetRequest](../../models/operations/c1apidirectoryv1directoryservicegetrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.C1APIDirectoryV1DirectoryServiceGetResponse](../../models/operations/c1apidirectoryv1directoryservicegetresponse.md)**


## list

List directories.

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

req = operations.C1APIDirectoryV1DirectoryServiceListRequest()

res = s.directory.list(req)

if res.directory_service_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.C1APIDirectoryV1DirectoryServiceListRequest](../../models/operations/c1apidirectoryv1directoryservicelistrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.C1APIDirectoryV1DirectoryServiceListResponse](../../models/operations/c1apidirectoryv1directoryservicelistresponse.md)**

