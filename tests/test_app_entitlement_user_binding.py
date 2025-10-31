import pytest
import os
from conftest import sdk_instance
from sdk.models import operations


class TestAppEntitlementUserBinding:
    """Test cases for AppEntitlementUserBinding functionality."""
    
    def test_list_app_users_for_identity_with_grant_should_return_status_200_and_valid_response(self):
        """Test that list_app_users_for_identity_with_grant returns status 200 and valid response."""
        app_id = os.getenv('C1_APP_ID')
        app_entitlement_id = os.getenv('C1_APP_ENTITLEMENT_ID')
        identity_user_id = os.getenv('C1_IDENTITY_USER_ID')
        
        if not app_id or not app_entitlement_id or not identity_user_id:
            pytest.skip("C1_APP_ID, C1_APP_ENTITLEMENT_ID, or C1_IDENTITY_USER_ID not set")
        
        req = operations.C1APIAppV1AppEntitlementUserBindingServiceListAppUsersForIdentityWithGrantRequest(
            app_id=app_id,
            app_entitlement_id=app_entitlement_id,
            identity_user_id=identity_user_id
        )
        res = sdk_instance.app_entitlement_user_binding.list_app_users_for_identity_with_grant(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_app_users_for_identity_with_grant_response is not None
