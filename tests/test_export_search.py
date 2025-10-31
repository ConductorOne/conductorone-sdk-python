from conftest import sdk_instance, shared


class TestExportSearch:
    """Test cases for ExportSearch functionality."""
    
    def test_exports_search_search_should_return_status_200_and_valid_response(self):
        """Test that exports_search_search returns status 200 and valid response."""
        res = sdk_instance.exports_search.search(request=shared.ExportsSearchServiceSearchRequest(page_size=1))
        
        assert res is not None
        assert res.status_code == 200
        assert res.exports_search_service_search_response is not None
