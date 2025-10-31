# OrgDomain
(*org_domain*)

## Overview

### Available Operations

* [list](#list) - List
* [update](#update) - Update

## list

Invokes the c1.api.settings.v1.OrgDomainService.List method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.settings.v1.OrgDomainService.List" method="get" path="/api/v1/settings/domains" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.org_domain.list()

    assert res.list_org_domains_response is not None

    # Handle response
    print(res.list_org_domains_response)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.C1APISettingsV1OrgDomainServiceListRequest](../../models/operations/c1apisettingsv1orgdomainservicelistrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.C1APISettingsV1OrgDomainServiceListResponse](../../models/operations/c1apisettingsv1orgdomainservicelistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Invokes the c1.api.settings.v1.OrgDomainService.Update method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.settings.v1.OrgDomainService.Update" method="put" path="/api/v1/settings/domains" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.org_domain.update()

    assert res.update_org_domain_response is not None

    # Handle response
    print(res.update_org_domain_response)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.UpdateOrgDomainRequest](../../models/shared/updateorgdomainrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.C1APISettingsV1OrgDomainServiceUpdateResponse](../../models/operations/c1apisettingsv1orgdomainserviceupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |