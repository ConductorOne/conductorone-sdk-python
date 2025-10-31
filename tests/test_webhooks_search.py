from conftest import sdk_instance, shared


class TestWebhooksSearch:
    """Test cases for WebhooksSearch functionality."""
    
    def test_search_should_return_status_200_and_valid_response(self):
        """Test that search returns status 200 and valid response."""
        req = shared.WebhooksSearchRequest(page_size=1)
        res = sdk_instance.webhooks_search.search(request=req)
        
        assert res is not None
        assert res.status_code == 200
        assert res.webhooks_search_response is not None
