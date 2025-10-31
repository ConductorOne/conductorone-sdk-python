import pytest
from conftest import sdk_instance, shared
from sdk.models import operations


class TestApps:
    """Test cases for Apps functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        req = operations.C1APIAppV1AppsListRequest(page_size=1)
        res = sdk_instance.apps.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_apps_response is not None
    
    def test_create_and_delete_app(self):
        """Test creating and deleting an app."""
        # Create app
        create_req = shared.CreateAppRequest(
            display_name='SDK Test App Python',
            description='Created by Python tests'
        )
        create_res = sdk_instance.apps.create(request=create_req)
        
        assert create_res is not None
        assert create_res.status_code == 200
        assert create_res.create_app_response is not None
        
        # Get the created app ID
        app_id = create_res.create_app_response.app.id if create_res.create_app_response.app else None
        
        if app_id:
            # Delete the app
            delete_req = operations.C1APIAppV1AppsDeleteRequest(
                id=app_id,
                delete_app_request=shared.DeleteAppRequest())
            delete_res = sdk_instance.apps.delete(request=delete_req)
            
            assert delete_res is not None
            assert delete_res.status_code == 200
    
    def test_get_app(self):
        """Test getting an app by ID."""
        # First list apps to get an ID
        list_req = operations.C1APIAppV1AppsListRequest(page_size=1)
        list_res = sdk_instance.apps.list(request=list_req)
        
        if list_res.list_apps_response and list_res.list_apps_response.list:
            app_id = list_res.list_apps_response.list[0].id
            
            # Get the specific app
            get_req = operations.C1APIAppV1AppsGetRequest(id=app_id or '')
            get_res = sdk_instance.apps.get(request=get_req)
            
            assert get_res is not None
            assert get_res.status_code == 200
            assert get_res.get_app_response is not None
            if get_res.get_app_response.app:
                assert get_res.get_app_response.app.id == app_id
            else:
                pytest.fail("App not found")
