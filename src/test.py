from sdk.models import shared

from src import sdk
if __name__ == "__main__":
      s = sdk.SDK(security=shared.SecuritySource())

    s = sdk_with_credentials("outstanding-werewolf-26337@c1dev.anthony.dev.ductone.com/pcc", "secret-token:conductorone.com:v1:eyJrdHkiOiJPS1AiLCJjcnYiOiJFZDI1NTE5IiwieCI6IlFWWjVIejJuTjFlcm1PNXdtaGNsQThpRTVRQjlZOTQ4a1hyU3BuWjR5NkkiLCJkIjoiUDhucUxCZlo0UnZPTHM3MDdhU1JYbXBDY3c0QU1ZejU5bE9Wb0tQQTFLTSJ9",token_url="https://c1dev.anthony.dev.ductone.com:2443/", server_url ="https://c1dev.anthony.dev.ductone.com:2443/")
    req = shared.AppEntitlementSearchServiceSearchRequest(
        only_get_expiring=False,
        page_size=20,
    )

    res = s.app_entitlement_search.search(req)
    print(res)
