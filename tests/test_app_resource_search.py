from conftest import sdk_instance, shared

class TestAppResourceSearch:
    """Test cases for AppResourceSearch functionality."""
    
    def test_search_should_return_status_200_and_valid_response(self):
        """Test that search returns status 200 and valid response."""
        req = shared.SearchAppResourcesRequest(page_size=10)
        res = sdk_instance.app_resource_search.search_app_resources(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_app_resources_response is not None
    
    def test_search_with_page_size(self):
        """Test app resource search with specific page size."""
        req = shared.SearchAppResourcesRequest(page_size=5)
        res = sdk_instance.app_resource_search.search_app_resources(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_app_resources_response is not None
        
        # Check that we get a response with list
        response_data = res.search_app_resources_response
        if response_data.list is not None:
            assert len(response_data.list or []) <= 5  # Should respect page size
