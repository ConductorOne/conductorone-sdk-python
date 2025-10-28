import pytest
import os
from conftest import sdk_instance
from sdk.models import operations


class TestAppEntitlementsProxy:
    """Test cases for AppEntitlementsProxy functionality."""
    
    def test_get_should_return_status_200_and_valid_response(self):
        """Test that get returns status 200 and valid response."""
        src_app_id = os.getenv('C1_APP_ID')
        dst_app_id = os.getenv('C1_DST_APP_ID')
        src_app_entitlement_id = os.getenv('C1_APP_ENTITLEMENT_ID')
        dst_app_entitlement_id = os.getenv('C1_DST_APP_ENTITLEMENT_ID')
        
        if not src_app_id or not dst_app_id or not src_app_entitlement_id or not dst_app_entitlement_id:
            pytest.skip("C1_APP_ID, C1_DST_APP_ID, C1_APP_ENTITLEMENT_ID, or C1_DST_APP_ENTITLEMENT_ID not set")
        
        req = operations.C1APIAppV1AppEntitlementsProxyGetRequest(
            src_app_id=src_app_id,
            dst_app_id=dst_app_id,
            src_app_entitlement_id=src_app_entitlement_id,
            dst_app_entitlement_id=dst_app_entitlement_id
        )
        res = sdk_instance.app_entitlements_proxy.get(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.get_app_entitlement_proxy_response is not None
