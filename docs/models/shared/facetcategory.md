# FacetCategory

The FacetCategory indicates a grouping of facets by type. For example, facets "OnePassword" and "Okta" would group under an "Apps" category.

This message contains a oneof named item. Only a single field of the following list may be set at a time:
  - value
  - range



## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `facet_range_item`                                                           | [Optional[shared.FacetRangeItem]](undefined/models/shared/facetrangeitem.md) | :heavy_minus_sign:                                                           | The FacetRangeItem message.                                                  |
| `facet_value_item`                                                           | [Optional[shared.FacetValueItem]](undefined/models/shared/facetvalueitem.md) | :heavy_minus_sign:                                                           | The FacetValueItem message.                                                  |
| `display_name`                                                               | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The display name of the category.                                            |
| `icon_url`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | An icon for the category.                                                    |
| `param`                                                                      | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The param that is being set when checking a facet in this category.          |