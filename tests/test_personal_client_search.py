from conftest import sdk_instance, shared


class TestPersonalClientSearch:
    """Test cases for PersonalClientSearch functionality."""
    
    def test_personal_client_search_search_should_return_status_200_and_valid_response(self):
        """Test that personal_client_search_search returns status 200 and valid response."""
        res = sdk_instance.personal_client_search.search(request=shared.PersonalClientSearchServiceSearchRequest(page_size=1))
        
        assert res is not None
        assert res.status_code == 200
        assert res.personal_client_search_service_search_response is not None
