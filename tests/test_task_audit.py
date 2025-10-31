import pytest
from conftest import sdk_instance, shared


class TestTaskAudit:
    """Test cases for TaskAudit functionality."""
    
    @pytest.mark.skip
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        res = sdk_instance.task_audit.list(request=shared.TaskAuditListRequest())
        
        assert res is not None
        assert res.status_code == 200
        assert res.task_audit_list_response is not None
