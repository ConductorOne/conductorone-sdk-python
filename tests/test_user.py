from conftest import sdk_instance
from sdk.models import operations


class TestUser:
    """Test cases for User functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        req = operations.C1APIUserV1UserServiceListRequest()
        res = sdk_instance.user.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.user_service_list_response is not None
