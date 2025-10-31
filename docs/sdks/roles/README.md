# Roles
(*roles*)

## Overview

### Available Operations

* [get](#get) - Get
* [list](#list) - List
* [update](#update) - Update

## get

Get a role by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.Roles.Get" method="get" path="/api/v1/iam/roles/{role_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.roles.get(request={
        "role_id": "<id>",
    })

    assert res.get_roles_response is not None

    # Handle response
    print(res.get_roles_response)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.C1APIIamV1RolesGetRequest](../../models/operations/c1apiiamv1rolesgetrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.C1APIIamV1RolesGetResponse](../../models/operations/c1apiiamv1rolesgetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List all roles for the current user.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.Roles.List" method="get" path="/api/v1/iam/roles" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.roles.list()

    assert res.list_roles_response is not None

    # Handle response
    print(res.list_roles_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.C1APIIamV1RolesListRequest](../../models/operations/c1apiiamv1roleslistrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.C1APIIamV1RolesListResponse](../../models/operations/c1apiiamv1roleslistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update a role by passing a Role object.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.iam.v1.Roles.Update" method="post" path="/api/v1/iam/roles/{role_id}" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.roles.update(request={
        "update_role_request": {},
        "role_id": "<id>",
    })

    assert res.update_roles_response is not None

    # Handle response
    print(res.update_roles_response)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.C1APIIamV1RolesUpdateRequest](../../models/operations/c1apiiamv1rolesupdaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.C1APIIamV1RolesUpdateResponse](../../models/operations/c1apiiamv1rolesupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |