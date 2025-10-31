from conftest import sdk_instance
from sdk.models import operations


class TestRequestCatalogManagement:
    """Test cases for RequestCatalogManagement functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        req = operations.C1APIRequestcatalogV1RequestCatalogManagementServiceListRequest(page_size=1)
        res = sdk_instance.request_catalog_management.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.request_catalog_management_service_list_response is not None
