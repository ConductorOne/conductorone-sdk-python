from conftest import sdk_instance


class TestAWSExternalIDSettings:
    """Test cases for AWSExternalIDSettings functionality."""
    
    def test_get_aws_external_id_settings_should_return_status_200_and_valid_response(self):
        """Test that get_aws_external_id_settings returns status 200 and valid response."""
        res = sdk_instance.aws_external_id_settings.get()
        
        assert res is not None
        assert res.status_code == 200
        assert res.get_aws_external_id_response is not None
    

