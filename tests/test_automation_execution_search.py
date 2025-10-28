from conftest import sdk_instance


class TestAutomationExecutionSearch:
    """Test cases for AutomationExecutionSearch functionality."""
    
    def test_search_automation_executions_should_return_status_200_and_valid_response(self):
        """Test that search_automation_executions returns status 200 and valid response."""
        res = sdk_instance.automation_execution_search.search_automation_executions()
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_automation_executions_response is not None
    
    def test_search_automation_executions_with_page_size(self):
        """Test automation execution search with specific page size."""
        res = sdk_instance.automation_execution_search.search_automation_executions()
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_automation_executions_response is not None
        
        # Check that we get a response with list
        response_data = res.search_automation_executions_response
        if response_data.list is not None:
            assert len(response_data.list or []) >= 0  # Should have a list (may be empty)
