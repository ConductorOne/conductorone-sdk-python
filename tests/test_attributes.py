from conftest import sdk_instance
from sdk.models import operations


class TestAttributes:
    """Test cases for Attributes functionality."""
    
    def test_list_attribute_types_should_return_status_200_and_valid_response(self):
        """Test that list_attribute_types returns status 200 and valid response."""
        req = operations.C1APIAttributeV1AttributesListAttributeTypesRequest(page_size=1)
        res = sdk_instance.attributes.list_attribute_types(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.list_attribute_types_response is not None
