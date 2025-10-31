from conftest import sdk_instance, shared


class TestSystemLog:
    """Test cases for SystemLog functionality."""
    
    def test_list_events_should_return_status_200_and_valid_response(self):
        """Test that list_events returns status 200 and valid response."""
        res = sdk_instance.system_log.list_events(request=shared.SystemLogServiceListEventsRequest(page_size=1))
        
        assert res is not None
        assert res.status_code == 200
        assert res.system_log_service_list_events_response is not None
