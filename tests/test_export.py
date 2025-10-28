from conftest import sdk_instance


class TestExport:
    """Test cases for Export functionality."""
    
    def test_list_exports_should_return_status_200_and_valid_response(self):
        """Test that list_exports returns status 200 and valid response."""
        res = sdk_instance.export.list()
        
        assert res is not None
        assert res.status_code == 200
        assert res.export_service_list_response is not None
