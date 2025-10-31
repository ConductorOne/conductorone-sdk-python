from conftest import sdk_instance, shared


class TestTaskSearch:
    """Test cases for TaskSearch functionality."""
    
    def test_search_should_return_status_200_and_valid_response(self):
        """Test that task search returns status 200 and valid response."""
        req = shared.TaskSearchRequest(page_size=10)
        res = sdk_instance.task_search.search(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.task_search_response is not None
    
    def test_search_with_page_size(self):
        """Test task search with specific page size."""
        req = shared.TaskSearchRequest(page_size=5)
        res = sdk_instance.task_search.search(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.task_search_response is not None
        
        # Check that we get a response with list
        response_data = res.task_search_response
        if response_data.list is not None:
            assert len(response_data.list or []) <= 5  # Should respect page size
