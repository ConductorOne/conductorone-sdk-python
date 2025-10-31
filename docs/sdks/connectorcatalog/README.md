# ConnectorCatalog
(*connector_catalog*)

## Overview

### Available Operations

* [configuration_schema](#configuration_schema) - Configuration Schema

## configuration_schema

Invokes the c1.api.integration.connector.v1.ConnectorCatalogService.ConfigurationSchema method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.integration.connector.v1.ConnectorCatalogService.ConfigurationSchema" method="post" path="/api/v1/connectorcatalog" -->
```python
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.connector_catalog.configuration_schema()

    assert res.connector_catalog_service_configuration_schema_response is not None

    # Handle response
    print(res.connector_catalog_service_configuration_schema_response)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [shared.ConnectorCatalogServiceConfigurationSchemaRequest](../../models/shared/connectorcatalogserviceconfigurationschemarequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[operations.C1APIIntegrationConnectorV1ConnectorCatalogServiceConfigurationSchemaResponse](../../models/operations/c1apiintegrationconnectorv1connectorcatalogserviceconfigurationschemaresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |