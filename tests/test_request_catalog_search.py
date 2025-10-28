from conftest import sdk_instance, shared


class TestRequestCatalogSearch:
    """Test cases for RequestCatalogSearch functionality."""
    
    def test_search_request_catalogs_should_return_status_200_and_valid_response(self):
        """Test that search_request_catalogs returns status 200 and valid response."""
        res = sdk_instance.request_catalog_search.search_entitlements(request=shared.RequestCatalogSearchServiceSearchEntitlementsRequest(page_size=1))
        
        assert res is not None
        assert res.status_code == 200
        assert res.request_catalog_search_service_search_entitlements_response is not None
