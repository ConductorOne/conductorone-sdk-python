# openapi

<!-- Start Summary [summary] -->
## Summary

ConductorOne API: The ConductorOne API is a HTTP API for managing ConductorOne resources.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#sdk-installation)
* [IDE Support](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#ide-support)
* [SDK Example Usage](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#sdk-example-usage)
* [Available Resources and Operations](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#available-resources-and-operations)
* [Retries](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#retries)
* [Error Handling](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#error-handling)
* [Server Selection](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#server-selection)
* [Custom HTTP Client](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#custom-http-client)
* [Authentication](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#authentication)
* [Debugging](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/ConductorOne/conductorone-sdk-python.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/ConductorOne/conductorone-sdk-python.git
```
<!-- End SDK Installation [installation] -->


```python
import sdk
from sdk.models import shared

s = sdk.sdk_with_credentials("CLIENT_ID", "CLIENT_SECRET")

req = shared.AppEntitlementSearchServiceSearchRequest(
    page_size=100,
)

res = s.app_entitlement_search.search(req)

if res.app_entitlement_search_service_search_response is not None:
    # For more decoding options, see `https://pypi.org/project/dataclasses-json/`
    res = res.app_entitlement_search_service_search_response.to_dict()
```
<!-- End SDK Example Usage -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [app_access_requests_defaults](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appaccessrequestsdefaults/README.md)

* [cancel_app_access_requests_defaults](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appaccessrequestsdefaults/README.md#cancel_app_access_requests_defaults) - Cancel App Access Requests Defaults
* [create_app_access_requests_defaults](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appaccessrequestsdefaults/README.md#create_app_access_requests_defaults) - Create App Access Requests Defaults
* [get_app_access_requests_defaults](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appaccessrequestsdefaults/README.md#get_app_access_requests_defaults) - Get App Access Requests Defaults

### [app_entitlement_owners](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementowners/README.md)

* [add](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementowners/README.md#add) - Add
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementowners/README.md#list) - List
* [remove](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementowners/README.md#remove) - Remove
* [set](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementowners/README.md#set) - Set

### [app_entitlement_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementsearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementsearch/README.md#search) - Search
* [search_app_entitlements_for_app_user](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementsearch/README.md#search_app_entitlements_for_app_user) - Search App Entitlements For App User
* [search_app_entitlements_with_expired](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementsearch/README.md#search_app_entitlements_with_expired) - Search App Entitlements With Expired

### [app_entitlement_user_binding](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementuserbinding/README.md)

* [list_app_users_for_identity_with_grant](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementuserbinding/README.md#list_app_users_for_identity_with_grant) - List App Users For Identity With Grant
* [search_grant_feed](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementuserbinding/README.md#search_grant_feed) - Search Grant Feed
* [search_past_grants](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlementuserbinding/README.md#search_past_grants) - Search Past Grants

### [app_entitlements](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#delete) - Delete
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#list) - List
* [list_for_app_resource](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#list_for_app_resource) - List For App Resource
* [list_for_app_user](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#list_for_app_user) - List For App User
* [~~list_users~~](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#list_users) - List Users :warning: **Deprecated**
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appentitlements/README.md#update) - Update

### [app_owners](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appowners/README.md)

* [add](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appowners/README.md#add) - Add
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appowners/README.md#list) - List
* [remove](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appowners/README.md#remove) - Remove
* [set](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appowners/README.md#set) - Set

### [app_report](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appreport/README.md)

* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appreport/README.md#list) - List

### [app_report_action](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appreportaction/README.md)

* [generate_report](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appreportaction/README.md#generate_report) - Generate Report

### [app_resource](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresource/README.md)

* [create_manually_managed_app_resource](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresource/README.md#create_manually_managed_app_resource) - Create Manually Managed App Resource
* [delete_manually_managed_app_resource](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresource/README.md#delete_manually_managed_app_resource) - Delete Manually Managed App Resource
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresource/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresource/README.md#list) - List
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresource/README.md#update) - Update

### [app_resource_owners](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourceowners/README.md)

* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourceowners/README.md#list) - List

### [app_resource_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcesearch/README.md)

* [search_app_resource_types](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcesearch/README.md#search_app_resource_types) - Search App Resource Types

### [app_resource_type](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcetype/README.md)

* [create_manually_managed_resource_type](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcetype/README.md#create_manually_managed_resource_type) - Create Manually Managed Resource Type
* [delete_manually_managed_resource_type](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcetype/README.md#delete_manually_managed_resource_type) - Delete Manually Managed Resource Type
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcetype/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcetype/README.md#list) - List
* [update_manually_managed_resource_type](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appresourcetype/README.md#update_manually_managed_resource_type) - Update Manually Managed Resource Type

### [app_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appsearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appsearch/README.md#search) - Search

### [app_usage_controls](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appusagecontrols/README.md)

* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appusagecontrols/README.md#get) - Get
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appusagecontrols/README.md#update) - Update

### [app_user](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appuser/README.md)

* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/appuser/README.md#update) - Update

### [apps](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/apps/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/apps/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/apps/README.md#delete) - Delete
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/apps/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/apps/README.md#list) - List
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/apps/README.md#update) - Update

### [attribute_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributesearch/README.md)

* [search_attribute_values](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributesearch/README.md#search_attribute_values) - Search Attribute Values

### [attributes](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributes/README.md)

* [create_attribute_value](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributes/README.md#create_attribute_value) - Create Attribute Value
* [delete_attribute_value](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributes/README.md#delete_attribute_value) - Delete Attribute Value
* [get_attribute_value](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributes/README.md#get_attribute_value) - Get Attribute Value
* [list_attribute_types](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributes/README.md#list_attribute_types) - List Attribute Types
* [list_attribute_values](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/attributes/README.md#list_attribute_values) - List Attribute Values

### [auth](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/auth/README.md)

* [introspect](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/auth/README.md#introspect) - Introspect

### [aws_external_id_settings](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/awsexternalidsettings/README.md)

* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/awsexternalidsettings/README.md#get) - Get

### [connector](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#create) - Create
* [create_delegated](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#create_delegated) - Create Delegated
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#delete) - Delete
* [force_sync](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#force_sync) - Force Sync
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#get) - Get
* [get_credentials](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#get_credentials) - Get Credentials
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#list) - List
* [revoke_credential](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#revoke_credential) - Revoke Credential
* [rotate_credential](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#rotate_credential) - Rotate Credential
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#update) - Update
* [update_delegated](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/connector/README.md#update_delegated) - Update Delegated

### [directory](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/directory/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/directory/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/directory/README.md#delete) - Delete
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/directory/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/directory/README.md#list) - List

### [export](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/export/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/export/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/export/README.md#delete) - Delete
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/export/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/export/README.md#list) - List
* [list_events](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/export/README.md#list_events) - List Events
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/export/README.md#update) - Update

### [exports_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/exportssearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/exportssearch/README.md#search) - Search

### [personal_client](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclient/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclient/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclient/README.md#delete) - Delete
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclient/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclient/README.md#list) - NOTE: Only shows personal clients for the current user.
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclient/README.md#update) - Update

### [personal_client_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclientsearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/personalclientsearch/README.md#search) - NOTE: Searches personal clients for all users

### [policies](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policies/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policies/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policies/README.md#delete) - Delete
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policies/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policies/README.md#list) - List
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policies/README.md#update) - Update

### [policy_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policysearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policysearch/README.md#search) - Search

### [policy_validate](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policyvalidate/README.md)

* [validate_cel](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/policyvalidate/README.md#validate_cel) - Validate Cel

### [request_catalog_management](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md)

* [add_access_entitlements](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#add_access_entitlements) - Add Access Entitlements
* [add_app_entitlements](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#add_app_entitlements) - Add App Entitlements
* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#delete) - Delete
* [force_run_bundle_automation](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#force_run_bundle_automation) - Force Run Bundle Automation
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#get) - Get
* [get_bundle_automation](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#get_bundle_automation) - Get Bundle Automation
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#list) - List
* [list_entitlements_for_access](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#list_entitlements_for_access) - List Entitlements For Access
* [list_entitlements_per_catalog](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#list_entitlements_per_catalog) - List Entitlements Per Catalog
* [remove_access_entitlements](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#remove_access_entitlements) - Remove Access Entitlements
* [remove_app_entitlements](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#remove_app_entitlements) - Remove App Entitlements
* [set_bundle_automation](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#set_bundle_automation) - Set Bundle Automation
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogmanagement/README.md#update) - Update

### [request_catalog_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogsearch/README.md)

* [search_entitlements](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/requestcatalogsearch/README.md#search_entitlements) - Search Entitlements

### [roles](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/roles/README.md)

* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/roles/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/roles/README.md#list) - List
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/roles/README.md#update) - Update


### [session_settings](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/sessionsettings/README.md)

* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/sessionsettings/README.md#get) - Get
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/sessionsettings/README.md#update) - Update

### [system_log](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/systemlog/README.md)

* [list_events](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/systemlog/README.md#list_events) - List Events

### [task](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/task/README.md)

* [create_grant_task](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/task/README.md#create_grant_task) - Create Grant Task
* [create_offboarding_task](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/task/README.md#create_offboarding_task) - Create Offboarding Task
* [create_revoke_task](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/task/README.md#create_revoke_task) - Create Revoke Task
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/task/README.md#get) - Get

### [task_actions](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md)

* [approve](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md#approve) - Approve
* [comment](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md#comment) - Comment
* [deny](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md#deny) - Deny
* [escalate_to_emergency_access](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md#escalate_to_emergency_access) - Escalate To Emergency Access
* [hard_reset](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md#hard_reset) - Hard Reset
* [reassign](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md#reassign) - Reassign
* [restart](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/taskactions/README.md#restart) - Restart

### [task_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/tasksearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/tasksearch/README.md#search) - Search

### [user](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/user/README.md)

* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/user/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/user/README.md#list) - List

### [user_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/usersearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/usersearch/README.md#search) - Search

### [webhooks](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhooks/README.md)

* [create](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhooks/README.md#create) - Create
* [delete](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhooks/README.md#delete) - Delete
* [get](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhooks/README.md#get) - Get
* [list](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhooks/README.md#list) - List
* [test](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhooks/README.md#test) - Test
* [update](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhooks/README.md#update) - Update

### [webhooks_search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhookssearch/README.md)

* [search](https://github.com/ConductorOne/conductorone-sdk-python/blob/master/docs/sdks/webhookssearch/README.md#search) - Search

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- No SDK Example Usage -->






<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_async` method may raise the following exceptions:

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

### Example

```python
from sdk import SDK
from sdk.models import errors, shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)

res = None
try:
    res = s.apps.create()

    if res.create_app_response is not None:
        # handle response
        pass

except errors.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://{tenantDomain}.conductor.one` | `tenantDomain` (default is `example`) |

#### Example

```python
from sdk import SDK
from sdk.models import shared

s = SDK(
    server_idx=0,
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)

res = s.apps.create()

if res.create_app_response is not None:
    # handle response
    pass

```

#### Variables

Some of the server options above contain variables. If you want to set the values of those variables, the following optional parameters are available when initializing the SDK client instance:
 * `tenant_domain: str`

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from sdk import SDK
from sdk.models import shared

s = SDK(
    server_url="https://{tenantDomain}.conductor.one",
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)

res = s.apps.create()

if res.create_app_response is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from sdk import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from sdk import SDK
from sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = SDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |
| `oauth`       | oauth2        | OAuth2 token  |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from sdk import SDK
from sdk.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)

res = s.apps.create()

if res.create_app_response is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from sdk import SDK
from sdk.models import shared
from sdk.utils import BackoffStrategy, RetryConfig

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)

res = s.apps.create(,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res.create_app_response is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from sdk import SDK
from sdk.models import shared
from sdk.utils import BackoffStrategy, RetryConfig

s = SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)

res = s.apps.create()

if res.create_app_response is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from sdk import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("sdk"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
