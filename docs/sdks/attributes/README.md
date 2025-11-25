# Attributes
(*attributes*)

## Overview

### Available Operations

* [create_attribute_value](#create_attribute_value) - Create Attribute Value
* [create_compliance_framework_attribute_value](#create_compliance_framework_attribute_value) - Create Compliance Framework Attribute Value
* [create_risk_level_attribute_value](#create_risk_level_attribute_value) - Create Risk Level Attribute Value
* [delete_attribute_value](#delete_attribute_value) - Delete Attribute Value
* [delete_compliance_framework_attribute_value](#delete_compliance_framework_attribute_value) - Delete Compliance Framework Attribute Value
* [delete_risk_level_attribute_value](#delete_risk_level_attribute_value) - Delete Risk Level Attribute Value
* [get_attribute_value](#get_attribute_value) - Get Attribute Value
* [get_compliance_framework_attribute_value](#get_compliance_framework_attribute_value) - Get Compliance Framework Attribute Value
* [get_risk_level_attribute_value](#get_risk_level_attribute_value) - Get Risk Level Attribute Value
* [list_attribute_types](#list_attribute_types) - List Attribute Types
* [list_attribute_values](#list_attribute_values) - List Attribute Values
* [list_compliance_frameworks](#list_compliance_frameworks) - List Compliance Frameworks
* [list_risk_levels](#list_risk_levels) - List Risk Levels

## create_attribute_value

Create a new attribute value.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.CreateAttributeValue" method="post" path="/api/v1/attributes" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.create_attribute_value()

    assert res.create_attribute_value_response is not None

    # Handle response
    print(res.create_attribute_value_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateAttributeValueRequest](../../models/shared/createattributevaluerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.C1APIAttributeV1AttributesCreateAttributeValueResponse](../../models/operations/c1apiattributev1attributescreateattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_compliance_framework_attribute_value

Create a compliance framework value.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.CreateComplianceFrameworkAttributeValue" method="post" path="/api/v1/attributes/compliance_frameworks" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.create_compliance_framework_attribute_value()

    assert res.create_compliance_framework_attribute_value_response is not None

    # Handle response
    print(res.create_compliance_framework_attribute_value_response)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [shared.CreateComplianceFrameworkAttributeValueRequest](../../models/shared/createcomplianceframeworkattributevaluerequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |

### Response

**[operations.C1APIAttributeV1AttributesCreateComplianceFrameworkAttributeValueResponse](../../models/operations/c1apiattributev1attributescreatecomplianceframeworkattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_risk_level_attribute_value

Create a risk level attribute.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.CreateRiskLevelAttributeValue" method="post" path="/api/v1/attributes/risk_levels" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.create_risk_level_attribute_value()

    assert res.create_risk_level_attribute_value_response is not None

    # Handle response
    print(res.create_risk_level_attribute_value_response)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [shared.CreateRiskLevelAttributeValueRequest](../../models/shared/createrisklevelattributevaluerequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.C1APIAttributeV1AttributesCreateRiskLevelAttributeValueResponse](../../models/operations/c1apiattributev1attributescreaterisklevelattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_attribute_value

Delete an attribute value by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.DeleteAttributeValue" method="delete" path="/api/v1/attribute/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.delete_attribute_value(request={
        "id": "<id>",
    })

    assert res.delete_attribute_value_response is not None

    # Handle response
    print(res.delete_attribute_value_response)

```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIAttributeV1AttributesDeleteAttributeValueRequest](../../models/operations/c1apiattributev1attributesdeleteattributevaluerequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `retries`                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                     | :heavy_minus_sign:                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                  |

### Response

**[operations.C1APIAttributeV1AttributesDeleteAttributeValueResponse](../../models/operations/c1apiattributev1attributesdeleteattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_compliance_framework_attribute_value

Delete an attribute value by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.DeleteComplianceFrameworkAttributeValue" method="delete" path="/api/v1/attributes/compliance_frameworks/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.delete_compliance_framework_attribute_value(request={
        "id": "<id>",
    })

    assert res.delete_compliance_framework_attribute_value_response is not None

    # Handle response
    print(res.delete_compliance_framework_attribute_value_response)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                  | [operations.C1APIAttributeV1AttributesDeleteComplianceFrameworkAttributeValueRequest](../../models/operations/c1apiattributev1attributesdeletecomplianceframeworkattributevaluerequest.md) | :heavy_check_mark:                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                 |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[operations.C1APIAttributeV1AttributesDeleteComplianceFrameworkAttributeValueResponse](../../models/operations/c1apiattributev1attributesdeletecomplianceframeworkattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_risk_level_attribute_value

Delete a risk level attribute value by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.DeleteRiskLevelAttributeValue" method="delete" path="/api/v1/attributes/risk_levels/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.delete_risk_level_attribute_value(request={
        "id": "<id>",
    })

    assert res.delete_risk_level_attribute_value_response is not None

    # Handle response
    print(res.delete_risk_level_attribute_value_response)

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.C1APIAttributeV1AttributesDeleteRiskLevelAttributeValueRequest](../../models/operations/c1apiattributev1attributesdeleterisklevelattributevaluerequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |
| `retries`                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                    |

### Response

**[operations.C1APIAttributeV1AttributesDeleteRiskLevelAttributeValueResponse](../../models/operations/c1apiattributev1attributesdeleterisklevelattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_attribute_value

Get an attribute value by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.GetAttributeValue" method="get" path="/api/v1/attributes/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.get_attribute_value(request={
        "id": "<id>",
    })

    assert res.get_attribute_value_response is not None

    # Handle response
    print(res.get_attribute_value_response)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIAttributeV1AttributesGetAttributeValueRequest](../../models/operations/c1apiattributev1attributesgetattributevaluerequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |

### Response

**[operations.C1APIAttributeV1AttributesGetAttributeValueResponse](../../models/operations/c1apiattributev1attributesgetattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_compliance_framework_attribute_value

Get an attribute value by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.GetComplianceFrameworkAttributeValue" method="get" path="/api/v1/attributes/compliance_frameworks/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.get_compliance_framework_attribute_value(request={
        "id": "<id>",
    })

    assert res.get_compliance_framework_attribute_value_response is not None

    # Handle response
    print(res.get_compliance_framework_attribute_value_response)

```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                            | [operations.C1APIAttributeV1AttributesGetComplianceFrameworkAttributeValueRequest](../../models/operations/c1apiattributev1attributesgetcomplianceframeworkattributevaluerequest.md) | :heavy_check_mark:                                                                                                                                                                   | The request object to use for the request.                                                                                                                                           |
| `retries`                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                  |

### Response

**[operations.C1APIAttributeV1AttributesGetComplianceFrameworkAttributeValueResponse](../../models/operations/c1apiattributev1attributesgetcomplianceframeworkattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_risk_level_attribute_value

Get a risk level attribute value by id.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.GetRiskLevelAttributeValue" method="get" path="/api/v1/attributes/risk_levels/{id}" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.get_risk_level_attribute_value(request={
        "id": "<id>",
    })

    assert res.get_risk_level_attribute_value_response is not None

    # Handle response
    print(res.get_risk_level_attribute_value_response)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.C1APIAttributeV1AttributesGetRiskLevelAttributeValueRequest](../../models/operations/c1apiattributev1attributesgetrisklevelattributevaluerequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |

### Response

**[operations.C1APIAttributeV1AttributesGetRiskLevelAttributeValueResponse](../../models/operations/c1apiattributev1attributesgetrisklevelattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_attribute_types

List all attribute types.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.ListAttributeTypes" method="get" path="/api/v1/attributes/types" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.list_attribute_types()

    assert res.list_attribute_types_response is not None

    # Handle response
    print(res.list_attribute_types_response)

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.C1APIAttributeV1AttributesListAttributeTypesRequest](../../models/operations/c1apiattributev1attributeslistattributetypesrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |
| `retries`                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                 | :heavy_minus_sign:                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                              |

### Response

**[operations.C1APIAttributeV1AttributesListAttributeTypesResponse](../../models/operations/c1apiattributev1attributeslistattributetypesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_attribute_values

List all attribute values for a given attribute type.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.ListAttributeValues" method="get" path="/api/v1/attributes/types/{attribute_type_id}/values" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.list_attribute_values(request={
        "attribute_type_id": "<id>",
    })

    assert res.list_attribute_values_response is not None

    # Handle response
    print(res.list_attribute_values_response)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.C1APIAttributeV1AttributesListAttributeValuesRequest](../../models/operations/c1apiattributev1attributeslistattributevaluesrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[operations.C1APIAttributeV1AttributesListAttributeValuesResponse](../../models/operations/c1apiattributev1attributeslistattributevaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_compliance_frameworks

Invokes the c1.api.attribute.v1.Attributes.ListComplianceFrameworks method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.ListComplianceFrameworks" method="get" path="/api/v1/attributes/compliance_frameworks" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.list_compliance_frameworks()

    assert res.list_compliance_frameworks_response is not None

    # Handle response
    print(res.list_compliance_frameworks_response)

```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.C1APIAttributeV1AttributesListComplianceFrameworksRequest](../../models/operations/c1apiattributev1attributeslistcomplianceframeworksrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |
| `retries`                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                             | :heavy_minus_sign:                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                          |

### Response

**[operations.C1APIAttributeV1AttributesListComplianceFrameworksResponse](../../models/operations/c1apiattributev1attributeslistcomplianceframeworksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_risk_levels

Invokes the c1.api.attribute.v1.Attributes.ListRiskLevels method.

### Example Usage

<!-- UsageSnippet language="python" operationID="c1.api.attribute.v1.Attributes.ListRiskLevels" method="get" path="/api/v1/attributes/risk_levels" -->
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.attributes.list_risk_levels()

    assert res.list_risk_levels_response is not None

    # Handle response
    print(res.list_risk_levels_response)

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.C1APIAttributeV1AttributesListRiskLevelsRequest](../../models/operations/c1apiattributev1attributeslistrisklevelsrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |

### Response

**[operations.C1APIAttributeV1AttributesListRiskLevelsResponse](../../models/operations/c1apiattributev1attributeslistrisklevelsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |