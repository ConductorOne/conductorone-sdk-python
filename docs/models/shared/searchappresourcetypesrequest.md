# SearchAppResourceTypesRequest

Search for app resources based on some filters.


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `app_ids`                                                     | List[*str*]                                                   | :heavy_minus_sign:                                            | A list of app IDs to restrict the search by.                  |
| `exclude_resource_type_ids`                                   | List[*str*]                                                   | :heavy_minus_sign:                                            | A list of resource type IDs to exclude from the search.       |
| `exclude_resource_type_trait_ids`                             | List[*str*]                                                   | :heavy_minus_sign:                                            | A list of resource type trait IDs to exclude from the search. |
| `page_size`                                                   | *Optional[int]*                                               | :heavy_minus_sign:                                            | The pageSize where 10 <= pageSize <= 100, default 25.         |
| `page_token`                                                  | *Optional[str]*                                               | :heavy_minus_sign:                                            | The pageToken field.                                          |
| `query`                                                       | *Optional[str]*                                               | :heavy_minus_sign:                                            | Fuzzy search the display name of resource types.              |
| `resource_type_ids`                                           | List[*str*]                                                   | :heavy_minus_sign:                                            | A list of resource type IDs to restrict the search by.        |
| `resource_type_trait_ids`                                     | List[*str*]                                                   | :heavy_minus_sign:                                            | A list of resource type trait IDs to restrict the search by.  |