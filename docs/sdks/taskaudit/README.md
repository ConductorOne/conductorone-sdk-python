# TaskAudit
(*task_audit*)

## Overview

### Available Operations

* [list](#list) - List

## list

Invokes the c1.api.task.v1.TaskAudit.List method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.task.v1.TaskAudit.List" method="post" path="/api/v1/task/audits" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.task_audit.list(request={})

    assert res.task_audit_list_response is not None

    # Handle response
    print(res.task_audit_list_response)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.TaskAuditListRequest](../../models/shared/taskauditlistrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[operations.C1APITaskV1TaskAuditListResponse](../../models/operations/c1apitaskv1taskauditlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |