# openapi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/ConductorOne/conductorone-sdk-python.git
```
<!-- End SDK Installation -->


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

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [apps](docs/sdks/apps/README.md)

* [create](docs/sdks/apps/README.md#create) - Create
* [delete](docs/sdks/apps/README.md#delete) - Delete
* [get](docs/sdks/apps/README.md#get) - Get
* [list](docs/sdks/apps/README.md#list) - List
* [update](docs/sdks/apps/README.md#update) - Update

### [connector](docs/sdks/connector/README.md)

* [create](docs/sdks/connector/README.md#create) - Create
* [create_delegated](docs/sdks/connector/README.md#create_delegated) - Create Delegated
* [delete](docs/sdks/connector/README.md#delete) - Delete
* [get](docs/sdks/connector/README.md#get) - Get
* [get_credentials](docs/sdks/connector/README.md#get_credentials) - Get Credentials
* [list](docs/sdks/connector/README.md#list) - List
* [revoke_credential](docs/sdks/connector/README.md#revoke_credential) - Revoke Credential
* [rotate_credential](docs/sdks/connector/README.md#rotate_credential) - Rotate Credential
* [update](docs/sdks/connector/README.md#update) - Update
* [update_delegated](docs/sdks/connector/README.md#update_delegated) - Update Delegated

### [app_entitlements](docs/sdks/appentitlements/README.md)

* [get](docs/sdks/appentitlements/README.md#get) - Get
* [list](docs/sdks/appentitlements/README.md#list) - List
* [list_for_app_resource](docs/sdks/appentitlements/README.md#list_for_app_resource) - List For App Resource
* [list_for_app_user](docs/sdks/appentitlements/README.md#list_for_app_user) - List For App User
* [list_users](docs/sdks/appentitlements/README.md#list_users) - List Users
* [update](docs/sdks/appentitlements/README.md#update) - Update

### [app_entitlement_user_binding](docs/sdks/appentitlementuserbinding/README.md)

* [list_app_users_for_identity_with_grant](docs/sdks/appentitlementuserbinding/README.md#list_app_users_for_identity_with_grant) - List App Users For Identity With Grant

### [app_entitlement_owners](docs/sdks/appentitlementowners/README.md)

* [add](docs/sdks/appentitlementowners/README.md#add) - Add
* [list](docs/sdks/appentitlementowners/README.md#list) - List
* [remove](docs/sdks/appentitlementowners/README.md#remove) - Remove
* [set](docs/sdks/appentitlementowners/README.md#set) - Set

### [app_owners](docs/sdks/appowners/README.md)

* [add](docs/sdks/appowners/README.md#add) - Add
* [list](docs/sdks/appowners/README.md#list) - List
* [remove](docs/sdks/appowners/README.md#remove) - Remove
* [set](docs/sdks/appowners/README.md#set) - Set

### [app_report](docs/sdks/appreport/README.md)

* [list](docs/sdks/appreport/README.md#list) - List

### [app_report_action](docs/sdks/appreportaction/README.md)

* [generate_report](docs/sdks/appreportaction/README.md#generate_report) - Generate Report

### [app_resource_type](docs/sdks/appresourcetype/README.md)

* [get](docs/sdks/appresourcetype/README.md#get) - Get
* [list](docs/sdks/appresourcetype/README.md#list) - List

### [app_resource](docs/sdks/appresource/README.md)

* [get](docs/sdks/appresource/README.md#get) - Get
* [list](docs/sdks/appresource/README.md#list) - List

### [app_resource_owners](docs/sdks/appresourceowners/README.md)

* [list](docs/sdks/appresourceowners/README.md#list) - List

### [app_usage_controls](docs/sdks/appusagecontrols/README.md)

* [get](docs/sdks/appusagecontrols/README.md#get) - Get
* [update](docs/sdks/appusagecontrols/README.md#update) - Update

### [app_user](docs/sdks/appuser/README.md)

* [update](docs/sdks/appuser/README.md#update) - Update

### [attributes](docs/sdks/attributes/README.md)

* [create_attribute_value](docs/sdks/attributes/README.md#create_attribute_value) - Create Attribute Value
* [delete_attribute_value](docs/sdks/attributes/README.md#delete_attribute_value) - Delete Attribute Value
* [get_attribute_value](docs/sdks/attributes/README.md#get_attribute_value) - Get Attribute Value
* [list_attribute_types](docs/sdks/attributes/README.md#list_attribute_types) - List Attribute Types
* [list_attribute_values](docs/sdks/attributes/README.md#list_attribute_values) - List Attribute Values

### [auth](docs/sdks/auth/README.md)

* [introspect](docs/sdks/auth/README.md#introspect) - Introspect

### [request_catalog_management](docs/sdks/requestcatalogmanagement/README.md)

* [add_access_entitlements](docs/sdks/requestcatalogmanagement/README.md#add_access_entitlements) - Add Access Entitlements
* [add_app_entitlements](docs/sdks/requestcatalogmanagement/README.md#add_app_entitlements) - Add App Entitlements
* [create](docs/sdks/requestcatalogmanagement/README.md#create) - Create
* [delete](docs/sdks/requestcatalogmanagement/README.md#delete) - Delete
* [get](docs/sdks/requestcatalogmanagement/README.md#get) - Get
* [list](docs/sdks/requestcatalogmanagement/README.md#list) - List
* [list_entitlements_for_access](docs/sdks/requestcatalogmanagement/README.md#list_entitlements_for_access) - List Entitlements For Access
* [list_entitlements_per_catalog](docs/sdks/requestcatalogmanagement/README.md#list_entitlements_per_catalog) - List Entitlements Per Catalog
* [remove_access_entitlements](docs/sdks/requestcatalogmanagement/README.md#remove_access_entitlements) - Remove Access Entitlements
* [remove_app_entitlements](docs/sdks/requestcatalogmanagement/README.md#remove_app_entitlements) - Remove App Entitlements
* [update](docs/sdks/requestcatalogmanagement/README.md#update) - Update

### [directory](docs/sdks/directory/README.md)

* [create](docs/sdks/directory/README.md#create) - Create
* [delete](docs/sdks/directory/README.md#delete) - Delete
* [get](docs/sdks/directory/README.md#get) - Get
* [list](docs/sdks/directory/README.md#list) - List

### [personal_client](docs/sdks/personalclient/README.md)

* [create](docs/sdks/personalclient/README.md#create) - Create

### [roles](docs/sdks/roles/README.md)

* [get](docs/sdks/roles/README.md#get) - Get
* [list](docs/sdks/roles/README.md#list) - List
* [update](docs/sdks/roles/README.md#update) - Update

### [policies](docs/sdks/policies/README.md)

* [create](docs/sdks/policies/README.md#create) - Create
* [delete](docs/sdks/policies/README.md#delete) - Delete
* [get](docs/sdks/policies/README.md#get) - Get
* [list](docs/sdks/policies/README.md#list) - List
* [update](docs/sdks/policies/README.md#update) - Update

### [policy_validate](docs/sdks/policyvalidate/README.md)

* [validate_cel](docs/sdks/policyvalidate/README.md#validate_cel) - Validate Cel

### [app_resource_search](docs/sdks/appresourcesearch/README.md)

* [search_app_resource_types](docs/sdks/appresourcesearch/README.md#search_app_resource_types) - Search App Resource Types

### [app_search](docs/sdks/appsearch/README.md)

* [search](docs/sdks/appsearch/README.md#search) - Search

### [attribute_search](docs/sdks/attributesearch/README.md)

* [search_attribute_values](docs/sdks/attributesearch/README.md#search_attribute_values) - Search Attribute Values

### [app_entitlement_search](docs/sdks/appentitlementsearch/README.md)

* [search](docs/sdks/appentitlementsearch/README.md#search) - Search

### [policy_search](docs/sdks/policysearch/README.md)

* [search](docs/sdks/policysearch/README.md#search) - Search

### [request_catalog_search](docs/sdks/requestcatalogsearch/README.md)

* [search_entitlements](docs/sdks/requestcatalogsearch/README.md#search_entitlements) - Search Entitlements

### [task_search](docs/sdks/tasksearch/README.md)

* [search](docs/sdks/tasksearch/README.md#search) - Search

### [user_search](docs/sdks/usersearch/README.md)

* [search](docs/sdks/usersearch/README.md#search) - Search

### [task](docs/sdks/task/README.md)

* [create_grant_task](docs/sdks/task/README.md#create_grant_task) - Create Grant Task
* [create_revoke_task](docs/sdks/task/README.md#create_revoke_task) - Create Revoke Task
* [get](docs/sdks/task/README.md#get) - Get

### [task_actions](docs/sdks/taskactions/README.md)

* [approve](docs/sdks/taskactions/README.md#approve) - Approve
* [comment](docs/sdks/taskactions/README.md#comment) - Comment
* [deny](docs/sdks/taskactions/README.md#deny) - Deny
* [escalate_to_emergency_access](docs/sdks/taskactions/README.md#escalate_to_emergency_access) - Escalate To Emergency Access
* [restart](docs/sdks/taskactions/README.md#restart) - Restart

### [user](docs/sdks/user/README.md)

* [get](docs/sdks/user/README.md#get) - Get
* [list](docs/sdks/user/README.md#list) - List
<!-- End SDK Available Operations -->

<!-- No SDK Example Usage -->


<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.CreateAppRequest(
    owners=[
        'string',
    ],
)

res = None
try:
    res = s.apps.create(req)

except (errors.SDKError) as e:
    print(e) # handle exception


if res.create_app_response is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://{tenantDomain}.conductor.one` | `tenantDomain` (default is `example`) |

#### Example

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    server_idx=0,
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.CreateAppRequest(
    owners=[
        'string',
    ],
)

res = s.apps.create(req)

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
import sdk
from sdk.models import shared

s = sdk.SDK(
    server_url="https://{tenantDomain}.conductor.one",
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.CreateAppRequest(
    owners=[
        'string',
    ],
)

res = s.apps.create(req)

if res.create_app_response is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |
| `oauth`       | oauth2        | OAuth2 token  |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)

req = shared.CreateAppRequest(
    owners=[
        'string',
    ],
)

res = s.apps.create(req)

if res.create_app_response is not None:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
