from conftest import sdk_instance, shared


class TestAttributeSearch:
    """Test cases for AttributeSearch functionality."""
    
    def test_search_should_return_status_200_and_valid_response(self):
        """Test that search returns status 200 and valid response."""
        req = shared.SearchAttributeValuesRequest(
            page_size=1
        )
        res = sdk_instance.attribute_search.search_attribute_values(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_attribute_values_response is not None