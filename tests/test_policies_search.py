from conftest import sdk_instance, shared


class TestPoliciesSearch:
    """Test cases for PoliciesSearch functionality."""
    
    def test_search_policies_should_return_status_200_and_valid_response(self):
        """Test that search_policies returns status 200 and valid response."""
        res = sdk_instance.policy_search.search(request=shared.SearchPoliciesRequest(page_size=1))
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_policies_response is not None
