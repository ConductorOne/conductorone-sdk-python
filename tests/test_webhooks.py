from conftest import sdk_instance
from sdk.models import operations


class TestWebhooks:
    """Test cases for Webhooks functionality."""
    
    def test_list_should_return_status_200_and_valid_response(self):
        """Test that list returns status 200 and valid response."""
        req = operations.C1APIWebhooksV1WebhooksServiceListRequest()
        res = sdk_instance.webhooks.list(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.webhooks_service_list_response is not None
