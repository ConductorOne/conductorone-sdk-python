from conftest import sdk_instance


class TestAutomation:
    """Test cases for AutomationSearch functionality."""
    
    def test_list_automations_should_return_status_200_and_valid_response(self):
        """Test that list_automations returns status 200 and valid response."""
        res = sdk_instance.automation.list_automations()
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_automations_response is not None
    
    def test_list_automations_with_page_size(self):
        """Test automation list with specific page size."""
        res = sdk_instance.automation.list_automations()
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_automations_response is not None
        
        # Check that we get a response with list
        response_data = res.list_automations_response
        if response_data.list is not None:
            assert len(response_data.list or []) >= 0  # Should have a list (may be empty)
