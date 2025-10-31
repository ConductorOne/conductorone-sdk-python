import pytest
import os
from conftest import sdk_instance
from sdk.models import operations


class TestAppResourceOwners:
    """Test cases for AppResourceOwners functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        app_id = os.getenv('C1_APP_ID')
        app_resource_id = os.getenv('C1_APP_RESOURCE_ID')
        app_resource_type_id = os.getenv('C1_APP_RESOURCE_TYPE_ID')
        
        if not app_id or not app_resource_id or not app_resource_type_id:
            pytest.skip("C1_APP_ID or C1_APP_RESOURCE_ID not set")
        
        req = operations.C1APIAppV1AppResourceOwnersListRequest(
            app_id=app_id,
            resource_id=app_resource_id,
            resource_type_id=app_resource_type_id,
            page_size=1
        )
        res = sdk_instance.appresource_owners.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_app_resource_owners_response is not None
