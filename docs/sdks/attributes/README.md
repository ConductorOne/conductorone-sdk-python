# Attributes

### Available Operations

* [create_attribute_value](#create_attribute_value) - Create Attribute Value
* [delete_attribute_value](#delete_attribute_value) - Delete Attribute Value
* [get_attribute_value](#get_attribute_value) - Get Attribute Value
* [list_attribute_types](#list_attribute_types) - List Attribute Types
* [list_attribute_values](#list_attribute_values) - List Attribute Values

## create_attribute_value

Create a new attribute value.

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

req = shared.CreateAttributeValueRequest(
    attribute_type_id='occaecati',
    value='rerum',
)

res = s.attributes.create_attribute_value(req)

if res.create_attribute_value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.CreateAttributeValueRequest](../../models/shared/createattributevaluerequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.C1APIAttributeV1AttributesCreateAttributeValueResponse](../../models/operations/c1apiattributev1attributescreateattributevalueresponse.md)**


## delete_attribute_value

Delete an attribute value by id.

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

req = operations.C1APIAttributeV1AttributesDeleteAttributeValueRequest(
    delete_attribute_value_request=shared.DeleteAttributeValueRequest(),
    id='3fe49a8d-9cbf-4486-b332-3f9b77f3a410',
)

res = s.attributes.delete_attribute_value(req)

if res.delete_attribute_value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.C1APIAttributeV1AttributesDeleteAttributeValueRequest](../../models/operations/c1apiattributev1attributesdeleteattributevaluerequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |


### Response

**[operations.C1APIAttributeV1AttributesDeleteAttributeValueResponse](../../models/operations/c1apiattributev1attributesdeleteattributevalueresponse.md)**


## get_attribute_value

Get an attribute value by id.

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

req = operations.C1APIAttributeV1AttributesGetAttributeValueRequest(
    id='0674ebf6-9280-4d1b-a77a-89ebf737ae42',
)

res = s.attributes.get_attribute_value(req)

if res.get_attribute_value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.C1APIAttributeV1AttributesGetAttributeValueRequest](../../models/operations/c1apiattributev1attributesgetattributevaluerequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.C1APIAttributeV1AttributesGetAttributeValueResponse](../../models/operations/c1apiattributev1attributesgetattributevalueresponse.md)**


## list_attribute_types

List all attribute types.

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

req = operations.C1APIAttributeV1AttributesListAttributeTypesRequest(
    page_size=206.51,
    page_token='amet',
)

res = s.attributes.list_attribute_types(req)

if res.list_attribute_types_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.C1APIAttributeV1AttributesListAttributeTypesRequest](../../models/operations/c1apiattributev1attributeslistattributetypesrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.C1APIAttributeV1AttributesListAttributeTypesResponse](../../models/operations/c1apiattributev1attributeslistattributetypesresponse.md)**


## list_attribute_values

List all attribute values for a given attribute type.

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

req = operations.C1APIAttributeV1AttributesListAttributeValuesRequest(
    attribute_type_id='optio',
    page_size=8815.86,
    page_token='ad',
)

res = s.attributes.list_attribute_values(req)

if res.list_attribute_values_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.C1APIAttributeV1AttributesListAttributeValuesRequest](../../models/operations/c1apiattributev1attributeslistattributevaluesrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.C1APIAttributeV1AttributesListAttributeValuesResponse](../../models/operations/c1apiattributev1attributeslistattributevaluesresponse.md)**

