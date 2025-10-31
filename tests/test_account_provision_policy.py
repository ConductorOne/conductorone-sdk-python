import pytest
from conftest import sdk_instance, shared


class TestAccountProvisionPolicy:
    """Test cases for AccountProvisionPolicy functionality."""
    
    @pytest.mark.skip
    def test_test_should_return_status_200_and_valid_response(self):
        """Test that test returns status 200 and valid response."""
        test_req = shared.TestAccountProvisionPolicyRequest(
            cel='true'
        )
        test_res = sdk_instance.account_provision_policy_test.test(request=test_req)
        
        assert test_res.status_code == 200
        assert test_res.test_account_provision_policy_response is not None