from conftest import sdk_instance


class TestAuth:
    """Test cases for Auth functionality."""
    
    def test_introspect_should_return_status_200_and_valid_response(self):
        """Test that introspect returns status 200 and valid response."""
        res = sdk_instance.auth.introspect()
        
        assert res is not None
        assert res.status_code == 200
        assert res.introspect_response is not None
