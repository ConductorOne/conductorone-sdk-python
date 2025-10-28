import pytest
from conftest import sdk_instance, shared


class TestStepUpProvider:
    """Test cases for StepUpProvider functionality."""
    
    @pytest.mark.skip
    def test_search_step_up_providers_should_return_status_200_and_valid_response(self):
        """Test that step_up returns status 200 and valid response."""
        res = sdk_instance.step_up_provider.search(request=shared.SearchStepUpProvidersRequest(page_size=1))
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_step_up_providers_response is not None
