import pytest
import os
from conftest import sdk_instance, shared
from sdk.models import operations


class TestAppUsageControls:
    """Test cases for AppUsageControls functionality."""
    
    def test_get_should_return_status_200_and_valid_response(self):
        """Test that get returns status 200 and valid response."""
        app_id = os.getenv('C1_APP_ID')
        if not app_id:
            pytest.skip("C1_APP_ID not set")
        
        req = operations.C1APIAppV1AppUsageControlsServiceGetRequest(app_id=app_id)
        res = sdk_instance.app_usage_controls.get(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.get_app_usage_controls_response is not None
