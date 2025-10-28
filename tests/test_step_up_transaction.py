import pytest
from conftest import sdk_instance, shared


class TestStepUpTransaction:
    """Test cases for StepUpTransaction functionality."""
    
    @pytest.mark.skip
    def test_search_step_up_transactions_should_return_status_200_and_valid_response(self):
        """Test that search_step_up_transactions returns status 200 and valid response."""
        res = sdk_instance.step_up_transaction.search(request=shared.SearchStepUpTransactionsRequest(page_size=1))
        
        assert res is not None
        assert res.status_code == 200
        assert res.search_step_up_transactions_response is not None
