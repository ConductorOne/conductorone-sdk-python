from conftest import sdk_instance


class TestSessionSettings:
    """Test cases for SessionSettings functionality."""
    
    def test_get_should_return_status_200_and_valid_response(self):
        """Test that get returns status 200 and valid response."""
        res = sdk_instance.session_settings.get()
        
        assert res is not None
        assert res.status_code == 200
        assert res.get_session_settings_response is not None
