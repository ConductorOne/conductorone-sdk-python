import pytest
import os
from conftest import sdk_instance
from sdk.models import operations


class TestAppResource:
    """Test cases for AppResource functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        # This test requires app ID and app resource type ID
        app_id = os.getenv('C1_APP_ID')
        app_resource_type_id = os.getenv('C1_APP_RESOURCE_TYPE_ID')
        
        if not app_id or not app_resource_type_id:
            pytest.skip("C1_APP_ID or C1_APP_RESOURCE_TYPE_ID not set")
        
        req = operations.C1APIAppV1AppResourceServiceListRequest(
            app_id=app_id,
            app_resource_type_id=app_resource_type_id,
            page_size=1
        )
        res = sdk_instance.app_resource.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.app_resource_service_list_response is not None
