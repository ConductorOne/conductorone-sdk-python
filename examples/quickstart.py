import os
import sdk  # package name is 'sdk'
from sdk.models import shared

s = sdk.sdk_with_credentials(
    client_id=os.environ["C1_CLIENT_ID"],
    client_secret=os.environ["C1_CLIENT_SECRET"],
    server_url=os.environ["C1_SERVER_URL"],
)
req = shared.AppEntitlementSearchServiceSearchRequest(app_ids=[], page_size=10)
res = s.app_entitlement_search.search(request=req)

if res and res.app_entitlement_search_service_search_response is not None and res.status_code == 200:
    print("Status code: ", res.status_code)
    entitlements = res.app_entitlement_search_service_search_response.list
    print(f"Success! Number of entitlements found: {len(entitlements) if entitlements else 0}")
else:
    print(f"No response or empty response. Status: {res.status_code if res else 'No response'}")