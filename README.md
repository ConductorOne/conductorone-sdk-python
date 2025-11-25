# openapi

<!-- Start Summary [summary] -->
## Summary

ConductorOne API: The ConductorOne API is a HTTP API for managing ConductorOne resources.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [openapi](#openapi)
  * [SDK Installation](#sdk-installation)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [IDE Support](#ide-support)
  * [Authentication](#authentication)
  * [Pagination](#pagination)
  * [Retries](#retries)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+https://github.com/ConductorOne/conductorone-sdk-python.git
```

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

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from conductorone-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "conductorone-sdk",
# ]
# ///

from conductorone_sdk import SDK

sdk = SDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [access_conflict](docs/sdks/accessconflict/README.md)

* [create_monitor](docs/sdks/accessconflict/README.md#create_monitor) - Create Monitor
* [delete_monitor](docs/sdks/accessconflict/README.md#delete_monitor) - Delete Monitor
* [get_monitor](docs/sdks/accessconflict/README.md#get_monitor) - Get Monitor
* [update_monitor](docs/sdks/accessconflict/README.md#update_monitor) - Update Monitor

### [account_provision_policy_test](docs/sdks/accountprovisionpolicytest/README.md)

* [test](docs/sdks/accountprovisionpolicytest/README.md#test) - Test

### [app_access_requests_defaults](docs/sdks/appaccessrequestsdefaults/README.md)

* [cancel_app_access_requests_defaults](docs/sdks/appaccessrequestsdefaults/README.md#cancel_app_access_requests_defaults) - Cancel App Access Requests Defaults
* [create_app_access_requests_defaults](docs/sdks/appaccessrequestsdefaults/README.md#create_app_access_requests_defaults) - Create App Access Requests Defaults
* [get_app_access_requests_defaults](docs/sdks/appaccessrequestsdefaults/README.md#get_app_access_requests_defaults) - Get App Access Requests Defaults

### [app_entitlement_monitor_binding](docs/sdks/appentitlementmonitorbinding/README.md)

* [create_app_entitlement_monitor_binding](docs/sdks/appentitlementmonitorbinding/README.md#create_app_entitlement_monitor_binding) - Create App Entitlement Monitor Binding
* [delete_app_entitlement_monitor_binding](docs/sdks/appentitlementmonitorbinding/README.md#delete_app_entitlement_monitor_binding) - Delete App Entitlement Monitor Binding
* [get_app_entitlement_monitor_binding](docs/sdks/appentitlementmonitorbinding/README.md#get_app_entitlement_monitor_binding) - Get App Entitlement Monitor Binding

### [app_entitlement_owners](docs/sdks/appentitlementowners/README.md)

* [add](docs/sdks/appentitlementowners/README.md#add) - Add
* [delete](docs/sdks/appentitlementowners/README.md#delete) - Delete
* [list](docs/sdks/appentitlementowners/README.md#list) - List
* [list_owner_i_ds](docs/sdks/appentitlementowners/README.md#list_owner_i_ds) - List Owner I Ds
* [remove](docs/sdks/appentitlementowners/README.md#remove) - Remove
* [set](docs/sdks/appentitlementowners/README.md#set) - Set

### [app_entitlement_search](docs/sdks/appentitlementsearch/README.md)

* [search](docs/sdks/appentitlementsearch/README.md#search) - Search
* [search_app_entitlements_for_app_user](docs/sdks/appentitlementsearch/README.md#search_app_entitlements_for_app_user) - Search App Entitlements For App User
* [search_app_entitlements_with_expired](docs/sdks/appentitlementsearch/README.md#search_app_entitlements_with_expired) - Search App Entitlements With Expired
* [search_grants](docs/sdks/appentitlementsearch/README.md#search_grants) - Search Grants

### [app_entitlement_user_binding](docs/sdks/appentitlementuserbinding/README.md)

* [list_app_users_for_identity_with_grant](docs/sdks/appentitlementuserbinding/README.md#list_app_users_for_identity_with_grant) - List App Users For Identity With Grant
* [remove_grant_duration](docs/sdks/appentitlementuserbinding/README.md#remove_grant_duration) - Remove Grant Duration
* [search_grant_feed](docs/sdks/appentitlementuserbinding/README.md#search_grant_feed) - Search Grant Feed
* [search_past_grants](docs/sdks/appentitlementuserbinding/README.md#search_past_grants) - Search Past Grants
* [update_grant_duration](docs/sdks/appentitlementuserbinding/README.md#update_grant_duration) - Update Grant Duration

### [app_entitlements](docs/sdks/appentitlements/README.md)

* [add_automation_exclusion](docs/sdks/appentitlements/README.md#add_automation_exclusion) - Add Automation Exclusion
* [add_manually_managed_members](docs/sdks/appentitlements/README.md#add_manually_managed_members) - Add Manually Managed Members
* [create](docs/sdks/appentitlements/README.md#create) - Create
* [create_automation](docs/sdks/appentitlements/README.md#create_automation) - Create Automation
* [delete](docs/sdks/appentitlements/README.md#delete) - Delete
* [delete_automation](docs/sdks/appentitlements/README.md#delete_automation) - Delete Automation
* [get](docs/sdks/appentitlements/README.md#get) - Get
* [get_automation](docs/sdks/appentitlements/README.md#get_automation) - Get Automation
* [list](docs/sdks/appentitlements/README.md#list) - List
* [list_automation_exclusions](docs/sdks/appentitlements/README.md#list_automation_exclusions) - List Automation Exclusions
* [list_for_app_resource](docs/sdks/appentitlements/README.md#list_for_app_resource) - List For App Resource
* [list_for_app_user](docs/sdks/appentitlements/README.md#list_for_app_user) - List For App User
* [~~list_users~~](docs/sdks/appentitlements/README.md#list_users) - List Users :warning: **Deprecated**
* [remove_automation_exclusion](docs/sdks/appentitlements/README.md#remove_automation_exclusion) - Remove Automation Exclusion
* [remove_entitlement_membership](docs/sdks/appentitlements/README.md#remove_entitlement_membership) - Remove Entitlement Membership
* [update](docs/sdks/appentitlements/README.md#update) - Update
* [update_automation](docs/sdks/appentitlements/README.md#update_automation) - Update Automation

### [app_entitlements_proxy](docs/sdks/appentitlementsproxy/README.md)

* [create](docs/sdks/appentitlementsproxy/README.md#create) - Create
* [delete](docs/sdks/appentitlementsproxy/README.md#delete) - Delete
* [get](docs/sdks/appentitlementsproxy/README.md#get) - Get

### [app_owners](docs/sdks/appowners/README.md)

* [add](docs/sdks/appowners/README.md#add) - Add
* [delete](docs/sdks/appowners/README.md#delete) - Delete
* [list](docs/sdks/appowners/README.md#list) - List
* [list_owner_i_ds](docs/sdks/appowners/README.md#list_owner_i_ds) - List Owner I Ds
* [remove](docs/sdks/appowners/README.md#remove) - Remove
* [set](docs/sdks/appowners/README.md#set) - Set

### [app_report](docs/sdks/appreport/README.md)

* [list](docs/sdks/appreport/README.md#list) - List

### [app_report_action](docs/sdks/appreportaction/README.md)

* [generate_report](docs/sdks/appreportaction/README.md#generate_report) - Generate Report

### [app_resource](docs/sdks/appresource/README.md)

* [create_manually_managed_app_resource](docs/sdks/appresource/README.md#create_manually_managed_app_resource) - Create Manually Managed App Resource
* [delete_manually_managed_app_resource](docs/sdks/appresource/README.md#delete_manually_managed_app_resource) - Delete Manually Managed App Resource
* [get](docs/sdks/appresource/README.md#get) - Get
* [list](docs/sdks/appresource/README.md#list) - List
* [update](docs/sdks/appresource/README.md#update) - Update

### [app_resource_owners](docs/sdks/appresourceowners/README.md)

* [add](docs/sdks/appresourceowners/README.md#add) - Add
* [delete](docs/sdks/appresourceowners/README.md#delete) - Delete
* [list](docs/sdks/appresourceowners/README.md#list) - List
* [list_owner_i_ds](docs/sdks/appresourceowners/README.md#list_owner_i_ds) - List Owner I Ds
* [remove](docs/sdks/appresourceowners/README.md#remove) - Remove
* [set](docs/sdks/appresourceowners/README.md#set) - Set

### [app_resource_search](docs/sdks/appresourcesearch/README.md)

* [search_app_resource_types](docs/sdks/appresourcesearch/README.md#search_app_resource_types) - Search App Resource Types
* [search_app_resources](docs/sdks/appresourcesearch/README.md#search_app_resources) - Search App Resources

### [app_resource_type](docs/sdks/appresourcetype/README.md)

* [create_manually_managed_resource_type](docs/sdks/appresourcetype/README.md#create_manually_managed_resource_type) - Create Manually Managed Resource Type
* [delete_manually_managed_resource_type](docs/sdks/appresourcetype/README.md#delete_manually_managed_resource_type) - Delete Manually Managed Resource Type
* [get](docs/sdks/appresourcetype/README.md#get) - Get
* [list](docs/sdks/appresourcetype/README.md#list) - List
* [update_manually_managed_resource_type](docs/sdks/appresourcetype/README.md#update_manually_managed_resource_type) - Update Manually Managed Resource Type

### [app_search](docs/sdks/appsearch/README.md)

* [search](docs/sdks/appsearch/README.md#search) - Search

### [app_usage_controls](docs/sdks/appusagecontrols/README.md)

* [get](docs/sdks/appusagecontrols/README.md#get) - Get
* [update](docs/sdks/appusagecontrols/README.md#update) - Update

### [app_user](docs/sdks/appuser/README.md)

* [list](docs/sdks/appuser/README.md#list) - List
* [list_app_user_credentials](docs/sdks/appuser/README.md#list_app_user_credentials) - List App User Credentials
* [list_app_users_for_user](docs/sdks/appuser/README.md#list_app_users_for_user) - List App Users For User
* [search](docs/sdks/appuser/README.md#search) - Search
* [update](docs/sdks/appuser/README.md#update) - Update

### [apps](docs/sdks/apps/README.md)

* [create](docs/sdks/apps/README.md#create) - Create
* [delete](docs/sdks/apps/README.md#delete) - Delete
* [get](docs/sdks/apps/README.md#get) - Get
* [list](docs/sdks/apps/README.md#list) - List
* [update](docs/sdks/apps/README.md#update) - Update

### [attribute_search](docs/sdks/attributesearch/README.md)

* [search_attribute_values](docs/sdks/attributesearch/README.md#search_attribute_values) - Search Attribute Values

### [attributes](docs/sdks/attributes/README.md)

* [create_attribute_value](docs/sdks/attributes/README.md#create_attribute_value) - Create Attribute Value
* [create_compliance_framework_attribute_value](docs/sdks/attributes/README.md#create_compliance_framework_attribute_value) - Create Compliance Framework Attribute Value
* [create_risk_level_attribute_value](docs/sdks/attributes/README.md#create_risk_level_attribute_value) - Create Risk Level Attribute Value
* [delete_attribute_value](docs/sdks/attributes/README.md#delete_attribute_value) - Delete Attribute Value
* [delete_compliance_framework_attribute_value](docs/sdks/attributes/README.md#delete_compliance_framework_attribute_value) - Delete Compliance Framework Attribute Value
* [delete_risk_level_attribute_value](docs/sdks/attributes/README.md#delete_risk_level_attribute_value) - Delete Risk Level Attribute Value
* [get_attribute_value](docs/sdks/attributes/README.md#get_attribute_value) - Get Attribute Value
* [get_compliance_framework_attribute_value](docs/sdks/attributes/README.md#get_compliance_framework_attribute_value) - Get Compliance Framework Attribute Value
* [get_risk_level_attribute_value](docs/sdks/attributes/README.md#get_risk_level_attribute_value) - Get Risk Level Attribute Value
* [list_attribute_types](docs/sdks/attributes/README.md#list_attribute_types) - List Attribute Types
* [list_attribute_values](docs/sdks/attributes/README.md#list_attribute_values) - List Attribute Values
* [list_compliance_frameworks](docs/sdks/attributes/README.md#list_compliance_frameworks) - List Compliance Frameworks
* [list_risk_levels](docs/sdks/attributes/README.md#list_risk_levels) - List Risk Levels

### [auth](docs/sdks/auth/README.md)

* [introspect](docs/sdks/auth/README.md#introspect) - Introspect

### [automation](docs/sdks/automation/README.md)

* [create_automation](docs/sdks/automation/README.md#create_automation) - Create Automation
* [delete_automation](docs/sdks/automation/README.md#delete_automation) - Delete Automation
* [execute_automation](docs/sdks/automation/README.md#execute_automation) - Execute Automation
* [get_automation](docs/sdks/automation/README.md#get_automation) - Get Automation
* [list_automations](docs/sdks/automation/README.md#list_automations) - List Automations
* [update_automation](docs/sdks/automation/README.md#update_automation) - Update Automation

### [automation_execution](docs/sdks/automationexecution/README.md)

* [get_automation_execution](docs/sdks/automationexecution/README.md#get_automation_execution) - Get Automation Execution
* [list_automation_executions](docs/sdks/automationexecution/README.md#list_automation_executions) - List Automation Executions

### [automation_execution_actions](docs/sdks/automationexecutionactions/README.md)

* [terminate_automation](docs/sdks/automationexecutionactions/README.md#terminate_automation) - Terminate Automation

### [automation_execution_search](docs/sdks/automationexecutionsearch/README.md)

* [search_automation_executions](docs/sdks/automationexecutionsearch/README.md#search_automation_executions) - Search Automation Executions

### [automation_search](docs/sdks/automationsearch/README.md)

* [search_automation_template_versions](docs/sdks/automationsearch/README.md#search_automation_template_versions) - Search Automation Template Versions
* [search_automations](docs/sdks/automationsearch/README.md#search_automations) - Search Automations

### [aws_external_id_settings](docs/sdks/awsexternalidsettings/README.md)

* [get](docs/sdks/awsexternalidsettings/README.md#get) - Get

### [connector](docs/sdks/connector/README.md)

* [confirm_sync_valid](docs/sdks/connector/README.md#confirm_sync_valid) - Confirm Sync Valid
* [create](docs/sdks/connector/README.md#create) - Create
* [create_delegated](docs/sdks/connector/README.md#create_delegated) - Create Delegated
* [delete](docs/sdks/connector/README.md#delete) - Delete
* [force_sync](docs/sdks/connector/README.md#force_sync) - Force Sync
* [get](docs/sdks/connector/README.md#get) - Get
* [get_connector_sync_download_url](docs/sdks/connector/README.md#get_connector_sync_download_url) - Get Connector Sync Download Url
* [get_credentials](docs/sdks/connector/README.md#get_credentials) - Get Credentials
* [list](docs/sdks/connector/README.md#list) - List
* [pause_sync](docs/sdks/connector/README.md#pause_sync) - Pause Sync
* [resume_sync](docs/sdks/connector/README.md#resume_sync) - Resume Sync
* [revoke_credential](docs/sdks/connector/README.md#revoke_credential) - Revoke Credential
* [rotate_credential](docs/sdks/connector/README.md#rotate_credential) - Rotate Credential
* [update](docs/sdks/connector/README.md#update) - Update
* [update_delegated](docs/sdks/connector/README.md#update_delegated) - Update Delegated
* [validate_http_connector_config](docs/sdks/connector/README.md#validate_http_connector_config) - Validate Http Connector Config

### [connector_catalog](docs/sdks/connectorcatalog/README.md)

* [configuration_schema](docs/sdks/connectorcatalog/README.md#configuration_schema) - Configuration Schema

### [directory](docs/sdks/directory/README.md)

* [create](docs/sdks/directory/README.md#create) - Create
* [delete](docs/sdks/directory/README.md#delete) - Delete
* [get](docs/sdks/directory/README.md#get) - Get
* [list](docs/sdks/directory/README.md#list) - List
* [update](docs/sdks/directory/README.md#update) - Update

### [export](docs/sdks/export/README.md)

* [create](docs/sdks/export/README.md#create) - Create
* [delete](docs/sdks/export/README.md#delete) - Delete
* [get](docs/sdks/export/README.md#get) - Get
* [list](docs/sdks/export/README.md#list) - List
* [list_events](docs/sdks/export/README.md#list_events) - List Events
* [update](docs/sdks/export/README.md#update) - Update

### [exports_search](docs/sdks/exportssearch/README.md)

* [search](docs/sdks/exportssearch/README.md#search) - Search

### [functions](docs/sdks/functions/README.md)

* [create_function](docs/sdks/functions/README.md#create_function) - Create Function
* [create_tag](docs/sdks/functions/README.md#create_tag) - Create Tag
* [delete_function](docs/sdks/functions/README.md#delete_function) - Delete Function
* [get_function](docs/sdks/functions/README.md#get_function) - Get Function
* [get_function_secret_encryption_key](docs/sdks/functions/README.md#get_function_secret_encryption_key) - Get Function Secret Encryption Key
* [invoke](docs/sdks/functions/README.md#invoke) - Invoke
* [list_commits](docs/sdks/functions/README.md#list_commits) - List Commits
* [list_functions](docs/sdks/functions/README.md#list_functions) - List Functions
* [list_tags](docs/sdks/functions/README.md#list_tags) - List Tags
* [update_function](docs/sdks/functions/README.md#update_function) - Update Function

### [functions_invocation](docs/sdks/functionsinvocation/README.md)

* [get](docs/sdks/functionsinvocation/README.md#get) - Get
* [list](docs/sdks/functionsinvocation/README.md#list) - List

### [functions_search](docs/sdks/functionssearch/README.md)

* [search](docs/sdks/functionssearch/README.md#search) - Search

### [org_domain](docs/sdks/orgdomain/README.md)

* [list](docs/sdks/orgdomain/README.md#list) - List
* [update](docs/sdks/orgdomain/README.md#update) - Update

### [personal_client](docs/sdks/personalclient/README.md)

* [create](docs/sdks/personalclient/README.md#create) - Create
* [delete](docs/sdks/personalclient/README.md#delete) - Delete
* [get](docs/sdks/personalclient/README.md#get) - Get
* [list](docs/sdks/personalclient/README.md#list) - NOTE: Only shows personal clients for the current user.
* [update](docs/sdks/personalclient/README.md#update) - Update

### [personal_client_search](docs/sdks/personalclientsearch/README.md)

* [search](docs/sdks/personalclientsearch/README.md#search) - NOTE: Searches personal clients for all users

### [policies](docs/sdks/policies/README.md)

* [create](docs/sdks/policies/README.md#create) - Create
* [delete](docs/sdks/policies/README.md#delete) - Delete
* [get](docs/sdks/policies/README.md#get) - Get
* [list](docs/sdks/policies/README.md#list) - List
* [update](docs/sdks/policies/README.md#update) - Update

### [policy_search](docs/sdks/policysearch/README.md)

* [search](docs/sdks/policysearch/README.md#search) - Search

### [policy_validate](docs/sdks/policyvalidate/README.md)

* [validate_cel](docs/sdks/policyvalidate/README.md#validate_cel) - Validate Cel

### [request_catalog_management](docs/sdks/requestcatalogmanagement/README.md)

* [add_access_entitlements](docs/sdks/requestcatalogmanagement/README.md#add_access_entitlements) - Add Access Entitlements
* [add_app_entitlements](docs/sdks/requestcatalogmanagement/README.md#add_app_entitlements) - Add App Entitlements
* [create](docs/sdks/requestcatalogmanagement/README.md#create) - Create
* [create_bundle_automation](docs/sdks/requestcatalogmanagement/README.md#create_bundle_automation) - Create Bundle Automation
* [create_requestable_entry](docs/sdks/requestcatalogmanagement/README.md#create_requestable_entry) - Create Requestable Entry
* [delete](docs/sdks/requestcatalogmanagement/README.md#delete) - Delete
* [delete_bundle_automation](docs/sdks/requestcatalogmanagement/README.md#delete_bundle_automation) - Delete Bundle Automation
* [delete_requestable_entry](docs/sdks/requestcatalogmanagement/README.md#delete_requestable_entry) - Delete Requestable Entry
* [force_run_bundle_automation](docs/sdks/requestcatalogmanagement/README.md#force_run_bundle_automation) - Force Run Bundle Automation
* [get](docs/sdks/requestcatalogmanagement/README.md#get) - Get
* [get_bundle_automation](docs/sdks/requestcatalogmanagement/README.md#get_bundle_automation) - Get Bundle Automation
* [get_requestable_entry](docs/sdks/requestcatalogmanagement/README.md#get_requestable_entry) - Get Requestable Entry
* [list](docs/sdks/requestcatalogmanagement/README.md#list) - List
* [list_all_entitlement_ids_per_app](docs/sdks/requestcatalogmanagement/README.md#list_all_entitlement_ids_per_app) - List All Entitlement Ids Per App
* [list_entitlements_for_access](docs/sdks/requestcatalogmanagement/README.md#list_entitlements_for_access) - List Entitlements For Access
* [list_entitlements_per_catalog](docs/sdks/requestcatalogmanagement/README.md#list_entitlements_per_catalog) - List Entitlements Per Catalog
* [remove_access_entitlements](docs/sdks/requestcatalogmanagement/README.md#remove_access_entitlements) - Remove Access Entitlements
* [remove_app_entitlements](docs/sdks/requestcatalogmanagement/README.md#remove_app_entitlements) - Remove App Entitlements
* [resume_paused_bundle_automation](docs/sdks/requestcatalogmanagement/README.md#resume_paused_bundle_automation) - Resume Paused Bundle Automation
* [set_bundle_automation](docs/sdks/requestcatalogmanagement/README.md#set_bundle_automation) - Set Bundle Automation
* [update](docs/sdks/requestcatalogmanagement/README.md#update) - Update
* [update_app_entitlements](docs/sdks/requestcatalogmanagement/README.md#update_app_entitlements) - Update App Entitlements

### [request_catalog_search](docs/sdks/requestcatalogsearch/README.md)

* [search_entitlements](docs/sdks/requestcatalogsearch/README.md#search_entitlements) - Search Entitlements

### [request_schema](docs/sdks/requestschema/README.md)

* [create](docs/sdks/requestschema/README.md#create) - Create
* [create_entitlement_binding](docs/sdks/requestschema/README.md#create_entitlement_binding) - Create Entitlement Binding
* [delete](docs/sdks/requestschema/README.md#delete) - Delete
* [find_binding_for_app_entitlement](docs/sdks/requestschema/README.md#find_binding_for_app_entitlement) - Find Binding For App Entitlement
* [get](docs/sdks/requestschema/README.md#get) - Get
* [remove_entitlement_binding](docs/sdks/requestschema/README.md#remove_entitlement_binding) - Remove Entitlement Binding
* [update](docs/sdks/requestschema/README.md#update) - Update

### [roles](docs/sdks/roles/README.md)

* [get](docs/sdks/roles/README.md#get) - Get
* [list](docs/sdks/roles/README.md#list) - List
* [update](docs/sdks/roles/README.md#update) - Update

### [session_settings](docs/sdks/sessionsettings/README.md)

* [get](docs/sdks/sessionsettings/README.md#get) - Get
* [test_source_ip](docs/sdks/sessionsettings/README.md#test_source_ip) - Test Source Ip
* [update](docs/sdks/sessionsettings/README.md#update) - Update

### [step_up_provider](docs/sdks/stepupprovider/README.md)

* [create](docs/sdks/stepupprovider/README.md#create) - Create
* [delete](docs/sdks/stepupprovider/README.md#delete) - Delete
* [get](docs/sdks/stepupprovider/README.md#get) - Get
* [list](docs/sdks/stepupprovider/README.md#list) - List
* [search](docs/sdks/stepupprovider/README.md#search) - Search
* [test](docs/sdks/stepupprovider/README.md#test) - Test
* [update](docs/sdks/stepupprovider/README.md#update) - Update
* [update_secret](docs/sdks/stepupprovider/README.md#update_secret) - Update Secret

### [step_up_transaction](docs/sdks/stepuptransaction/README.md)

* [get](docs/sdks/stepuptransaction/README.md#get) - Get
* [search](docs/sdks/stepuptransaction/README.md#search) - Search

### [system_log](docs/sdks/systemlog/README.md)

* [list_events](docs/sdks/systemlog/README.md#list_events) - List Events

### [task](docs/sdks/task/README.md)

* [create_grant_task](docs/sdks/task/README.md#create_grant_task) - Create Grant Task
* [create_offboarding_task](docs/sdks/task/README.md#create_offboarding_task) - Create Offboarding Task
* [create_revoke_task](docs/sdks/task/README.md#create_revoke_task) - Create Revoke Task
* [get](docs/sdks/task/README.md#get) - Get

### [task_actions](docs/sdks/taskactions/README.md)

* [approve](docs/sdks/taskactions/README.md#approve) - Approve
* [approve_with_step_up](docs/sdks/taskactions/README.md#approve_with_step_up) - Approve With Step Up
* [close](docs/sdks/taskactions/README.md#close) - Close
* [comment](docs/sdks/taskactions/README.md#comment) - Comment
* [deny](docs/sdks/taskactions/README.md#deny) - Deny
* [escalate_to_emergency_access](docs/sdks/taskactions/README.md#escalate_to_emergency_access) - Escalate To Emergency Access
* [hard_reset](docs/sdks/taskactions/README.md#hard_reset) - Hard Reset
* [process_now](docs/sdks/taskactions/README.md#process_now) - Process Now
* [reassign](docs/sdks/taskactions/README.md#reassign) - Reassign
* [restart](docs/sdks/taskactions/README.md#restart) - Restart
* [skip_step](docs/sdks/taskactions/README.md#skip_step) - Skip Step
* [update_grant_duration](docs/sdks/taskactions/README.md#update_grant_duration) - Update Grant Duration
* [update_request_data](docs/sdks/taskactions/README.md#update_request_data) - Update Request Data

### [task_audit](docs/sdks/taskaudit/README.md)

* [list](docs/sdks/taskaudit/README.md#list) - List

### [task_search](docs/sdks/tasksearch/README.md)

* [search](docs/sdks/tasksearch/README.md#search) - Search

### [user](docs/sdks/user/README.md)

* [get](docs/sdks/user/README.md#get) - Get
* [get_user_profile_types](docs/sdks/user/README.md#get_user_profile_types) - Get User Profile Types
* [list](docs/sdks/user/README.md#list) - List
* [set_expiring_user_delegation_binding_by_admin](docs/sdks/user/README.md#set_expiring_user_delegation_binding_by_admin) - Set Expiring User Delegation Binding By Admin

### [user_search](docs/sdks/usersearch/README.md)

* [search](docs/sdks/usersearch/README.md#search) - Search

### [vault](docs/sdks/vault/README.md)

* [create](docs/sdks/vault/README.md#create) - Create
* [delete](docs/sdks/vault/README.md#delete) - Delete
* [get](docs/sdks/vault/README.md#get) - Get
* [update](docs/sdks/vault/README.md#update) - Update

### [webhooks](docs/sdks/webhooks/README.md)

* [create](docs/sdks/webhooks/README.md#create) - Create
* [delete](docs/sdks/webhooks/README.md#delete) - Delete
* [get](docs/sdks/webhooks/README.md#get) - Get
* [list](docs/sdks/webhooks/README.md#list) - List
* [test](docs/sdks/webhooks/README.md#test) - Test
* [update](docs/sdks/webhooks/README.md#update) - Update

### [webhooks_search](docs/sdks/webhookssearch/README.md)

* [search](docs/sdks/webhookssearch/README.md#search) - Search

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- No SDK Example Usage -->






<!-- Start Error Handling [errors] -->
## Error Handling

[`SDKBaseError`](./src/conductorone_sdk/models/errors/sdkbaseerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import errors, shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:
    res = None
    try:

        res = sdk.access_conflict.create_monitor()

        assert res.conflict_monitor is not None

        # Handle response
        print(res.conflict_monitor)


    except errors.SDKBaseError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`SDKBaseError`](./src/conductorone_sdk/models/errors/sdkbaseerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SDKBaseError`](./src/conductorone_sdk/models/errors/sdkbaseerror.py)**:
* [`ResponseValidationError`](./src/conductorone_sdk/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Server Variables

The default server `https://{tenantDomain}.conductor.one` contains variables and is set to `https://example.conductor.one` by default. To override default values, the following parameters are available when initializing the SDK client instance:

| Variable       | Parameter            | Default     | Description                                       |
| -------------- | -------------------- | ----------- | ------------------------------------------------- |
| `tenantDomain` | `tenant_domain: str` | `"example"` | The domain of the tenant to use for this request. |

#### Example

```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    server_idx=0,
    tenant_domain="example",
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.create_monitor()

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    server_url="https://example.conductor.one",
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.create_monitor()

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from conductorone_sdk import SDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = SDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from conductorone_sdk import SDK
from conductorone_sdk.httpclient import AsyncHttpClient
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



<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type   | Scheme       |
| ------------- | ------ | ------------ |
| `bearer_auth` | http   | HTTP Bearer  |
| `oauth`       | oauth2 | OAuth2 token |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.create_monitor()

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```
<!-- End Authentication [security] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.app_entitlement_search.search()

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared
from conductorone_sdk.utils import BackoffStrategy, RetryConfig


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.create_monitor(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared
from conductorone_sdk.utils import BackoffStrategy, RetryConfig


with SDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.create_monitor()

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)

```
<!-- End Retries [retries] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `SDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from conductorone_sdk import SDK
from conductorone_sdk.models import shared
def main():

    with SDK(
        security=shared.Security(
            bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
            oauth="<YOUR_OAUTH_HERE>",
        ),
    ) as sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with SDK(
        security=shared.Security(
            bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
            oauth="<YOUR_OAUTH_HERE>",
        ),
    ) as sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from conductorone_sdk import SDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = SDK(debug_logger=logging.getLogger("conductorone_sdk"))
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
