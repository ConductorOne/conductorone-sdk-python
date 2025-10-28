from conftest import sdk_instance, shared


class TestAppEntitlementSearch:
    """Test cases for AppEntitlementSearch functionality."""
    
    def test_search_should_return_status_200_and_valid_response(self):
        """Test that search returns status 200 and valid response."""
        req = shared.AppEntitlementSearchServiceSearchRequest(app_ids=[], page_size=10)
        res = sdk_instance.app_entitlement_search.search(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.app_entitlement_search_service_search_response is not None
    
    def test_search_grants_should_return_status_200_and_valid_response(self):
        """Test that searchGrants returns status 200 and valid response."""
        req = shared.AppEntitlementSearchServiceSearchGrantsRequest(app_ids=[], page_size=10)
        res = sdk_instance.app_entitlement_search.search_grants(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.app_entitlement_search_service_search_grants_response is not None
    
    def test_search_with_page_size(self):
        """Test search with specific page size."""
        req = shared.AppEntitlementSearchServiceSearchRequest(app_ids=[], page_size=5)
        res = sdk_instance.app_entitlement_search.search(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.app_entitlement_search_service_search_response is not None
        
        # Check that we get a response with list
        response_data = res.app_entitlement_search_service_search_response
        if response_data.list is not None:
            assert len(response_data.list or []) <= 5  # Should respect page size
