import pytest
import os
from conftest import sdk_instance
from sdk.models import operations


class TestAppEntitlementOwners:
    """Test cases for AppEntitlementOwners functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        app_id = os.getenv('C1_APP_ID')
        app_entitlement_id = os.getenv('C1_APP_ENTITLEMENT_ID')
        
        if not app_id or not app_entitlement_id:
            pytest.skip("C1_APP_ID or C1_APP_ENTITLEMENT_ID not set")
        
        req = operations.C1APIAppV1AppEntitlementOwnersListRequest(
            app_id=app_id,
            entitlement_id=app_entitlement_id,
            page_size=1
        )
        res = sdk_instance.app_entitlement_owners.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_app_entitlement_owners_response is not None
