import pytest
import os
from conftest import sdk_instance
from sdk.models import operations


class TestAppReports:
    """Test cases for AppReports functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        app_id = os.getenv('C1_APP_ID')
        if not app_id:
            pytest.skip("C1_APP_ID not set")
        
        req = operations.C1APIAppV1AppReportServiceListRequest(app_id=app_id, page_size=1)
        res = sdk_instance.app_report.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.app_report_service_list_response is not None
