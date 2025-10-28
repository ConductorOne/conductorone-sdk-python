from conftest import sdk_instance
from sdk.models import operations


class TestPolicies:
    """Test cases for Policies functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        req = operations.C1APIPolicyV1PoliciesListRequest(page_size=1)
        res = sdk_instance.policies.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_policy_response is not None
