from conftest import sdk_instance


class TestOrgDomain:
    """Test cases for OrgDomain functionality."""
    
    def test_list_org_domains_should_return_status_200_and_valid_response(self):
        """Test that list_org_domains returns status 200 and valid response."""
        res = sdk_instance.org_domain.list()
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_org_domains_response is not None
