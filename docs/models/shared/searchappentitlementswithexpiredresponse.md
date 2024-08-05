# SearchAppEntitlementsWithExpiredResponse

The SearchAppEntitlementsWithExpiredResponse message contains a list of results and a nextPageToken if applicable.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `list`                                                                                     | List[[shared.AppEntitlementWithExpired](../../models/shared/appentitlementwithexpired.md)] | :heavy_minus_sign:                                                                         | The list field.                                                                            |
| `next_page_token`                                                                          | *Optional[str]*                                                                            | :heavy_minus_sign:                                                                         | The nextPageToken field.                                                                   |