# ExternalTicketProvision

This provision step indicates that we should check an external ticket to provision this entitlement


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `app_id`                                                                          | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | The appId field.                                                                  |
| `connector_id`                                                                    | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | The connectorId field.                                                            |
| `external_ticket_provisioner_config_id`                                           | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | The externalTicketProvisionerConfigId field.                                      |
| `instructions`                                                                    | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | This field indicates a text body of instructions for the provisioner to indicate. |