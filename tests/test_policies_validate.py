from conftest import sdk_instance, shared


class TestPolicyValidate:
    """Test cases for PolicyValidate functionality."""
    
    def test_validate_cel_should_return_status_200_and_valid_response(self):
        """Test that validate_cel returns status 200 and valid response."""
        res = sdk_instance.policy_validate.validate_cel(request=shared.EditorValidateRequest(text="test"))
        
        assert res is not None
        assert res.status_code == 200
        assert res.editor_validate_response is not None
