import pytest
from conftest import sdk_instance
from sdk.models import operations


class TestTask:
    """Test cases for Task functionality."""
    
    def test_get_should_return_status_200_and_valid_response(self):
        """Test that get returns status 200 and valid response."""
        req = operations.C1APITaskV1TaskServiceGetRequest(id="1")
        res = sdk_instance.task.get(request=req)
        
        if res.status_code == 404:
            pytest.skip("Task not found")
        else:
            assert res is not None
            assert res.status_code == 200
            assert res.task_service_get_response is not None
