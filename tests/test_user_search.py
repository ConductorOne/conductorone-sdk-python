from conftest import sdk_instance, shared


class TestUserSearch:
    """Test cases for UserSearch functionality."""
    
    def test_search_should_return_status_200_and_valid_response(self):
        """Test that user search returns status 200 and valid response."""
        req = shared.SearchUsersRequest(page_size=10)
        res = sdk_instance.user_search.search(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_users_response is not None
    
    def test_search_with_page_size(self):
        """Test user search with specific page size."""
        req = shared.SearchUsersRequest(page_size=5)
        res = sdk_instance.user_search.search(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_users_response is not None
        
        # Check that we get a response with list
        response_data = res.search_users_response
        if response_data.list is not None:
            assert len(response_data.list or []) <= 5  # Should respect page size
