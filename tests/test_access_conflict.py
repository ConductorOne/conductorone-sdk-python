from conftest import sdk_instance, shared
from sdk.models import operations


class TestAccessConflict:
    """Test cases for AccessConflict functionality."""
    
    def test_create_monitor_should_return_status_200_and_valid_response(self):
        """Test that createMonitor returns status 200 and valid response."""
        # Create a monitor
        create_req = shared.ConflictMonitorCreateRequest(
            display_name='Test Monitor',
            description='Test Monitor Description'
        )
        create_res = sdk_instance.access_conflict.create_monitor(request=create_req)
        
        assert create_res.status_code == 200
        assert create_res.conflict_monitor is not None
        
        # Get the monitor ID and verify it exists
        monitor_id = create_res.conflict_monitor.id
        if monitor_id:
            get_req = operations.C1APIAccessconflictV1AccessConflictServiceGetMonitorRequest(id=monitor_id)
            get_res = sdk_instance.access_conflict.get_monitor(request=get_req)
            
            assert get_res.status_code == 200
            assert get_res.conflict_monitor is not None

            # Delete the monitor
            delete_req = operations.C1APIAccessconflictV1AccessConflictServiceDeleteMonitorRequest(
                id=monitor_id,
                conflict_monitor_delete_request=shared.ConflictMonitorDeleteRequest())
            delete_res = sdk_instance.access_conflict.delete_monitor(
                request=delete_req,
            )

            assert delete_res.status_code == 200
            assert delete_res.conflict_monitor_delete_response is not None

