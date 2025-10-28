from conftest import sdk_instance
from sdk.models import operations


class TestRoles:
    """Test cases for Roles functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        req = operations.C1APIIamV1RolesListRequest()
        res = sdk_instance.roles.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_roles_response is not None
