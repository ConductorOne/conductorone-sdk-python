from conftest import sdk_instance


class TestPersonalClient:
    """Test cases for PersonalClient functionality."""
    
    def test_list_personal_clients_should_return_status_200_and_valid_response(self):
        """Test that list_personal_clients returns status 200 and valid response."""
        res = sdk_instance.personal_client.list()
        
        assert res is not None
        assert res.status_code == 200
        assert res.personal_client_service_list_response is not None
