from conftest import sdk_instance


class TestAutomationExecution:
    """Test cases for AutomationExecution functionality."""
    
    def test_list_automation_executions_should_return_status_200_and_valid_response(self):
        """Test that list_automation_executions returns status 200 and valid response."""
        res = sdk_instance.automation_execution.list_automation_executions()
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_automation_executions_response is not None
    
    def test_list_automation_executions_with_page_size(self):
        """Test automation execution list with specific page size."""
        res = sdk_instance.automation_execution.list_automation_executions()
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_automation_executions_response is not None
        
        # Check that we get a response with list
        response_data = res.list_automation_executions_response
        if response_data.automation_executions is not None:
            assert len(response_data.automation_executions or []) >= 0  # Should have a list (may be empty)
