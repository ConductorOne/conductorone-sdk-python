import pytest
import os
from conftest import sdk_instance
from sdk.models import operations
from sdk.models import shared


class TestAppReportAction:
    """Test cases for AppReportAction functionality."""
    
    def test_generate_report_should_return_status_200_and_valid_response(self):
        """Test that generate report returns status 200 and valid response."""
        app_id = os.getenv('C1_APP_ID')
        if not app_id:
            pytest.skip("C1_APP_ID not set")
        
        req = operations.C1APIAppV1AppReportActionServiceGenerateReportRequest(
            app_id=app_id,
            app_actions_service_generate_report_request=shared.AppActionsServiceGenerateReportRequest())
        res = sdk_instance.app_report_action.generate_report(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.app_actions_service_generate_report_response is not None
