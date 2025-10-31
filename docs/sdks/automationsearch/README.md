# AutomationSearch
(*automation_search*)

## Overview

### Available Operations

* [search_automation_template_versions](#search_automation_template_versions) - Search Automation Template Versions
* [search_automations](#search_automations) - Search Automations

## search_automation_template_versions

Invokes the c1.api.automations.v1.AutomationSearchService.SearchAutomationTemplateVersions method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationSearchService.SearchAutomationTemplateVersions" method="post" path="/api/v1/automation_versions/search" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.automation_search.search_automation_template_versions(request={})

    assert res.search_automation_template_versions_response is not None

    # Handle response
    print(res.search_automation_template_versions_response)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [shared.SearchAutomationTemplateVersionsRequest](../../models/shared/searchautomationtemplateversionsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.C1APIAutomationsV1AutomationSearchServiceSearchAutomationTemplateVersionsResponse](../../models/operations/c1apiautomationsv1automationsearchservicesearchautomationtemplateversionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## search_automations

Invokes the c1.api.automations.v1.AutomationSearchService.SearchAutomations method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.automations.v1.AutomationSearchService.SearchAutomations" method="post" path="/api/v1/automations/search" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.automation_search.search_automations(request={})

    assert res.search_automations_response is not None

    # Handle response
    print(res.search_automations_response)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.SearchAutomationsRequest](../../models/shared/searchautomationsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.C1APIAutomationsV1AutomationSearchServiceSearchAutomationsResponse](../../models/operations/c1apiautomationsv1automationsearchservicesearchautomationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |