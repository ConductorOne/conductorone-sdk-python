# SDK Test Suite (pytest)

This directory contains end-to-end tests that exercise the generated SDK against a live ConductorOne environment. Tests use pytest and require valid API credentials and several resource identifiers from your org.

## Setup

1. Install dependencies:

Using **uv** (recommended):
```bash
uv sync --dev
```

Using **Poetry**:
```bash
poetry install --with dev
```

Using **pip**:
```bash
pip install -e ".[dev]"
```

2. Copy the environment template:
```bash
cp env.example .env.local
```

3. Fill in your ConductorOne credentials and test resource IDs in `.env.local`.

## How tests run
- Tests import a preconfigured SDK from `conftest.py`.
- `python-dotenv` loads credentials and IDs from `.env` / `.env.local`.
- Each test calls one or more SDK methods and asserts `status_code == 200` and a non-empty typed response.
- Some tests are conditional: if a required env var is not set, they log a skip message and do nothing.

Run all tests:
```bash
uv run pytest
# or
poetry run pytest
```

Run a specific test file:
```bash
uv run pytest tests/test_apps.py
```

Run a specific test class:
```bash
uv run pytest tests/test_apps.py::TestApps
```

Run a specific test method:
```bash
uv run pytest tests/test_apps.py::TestApps::test_list_should_return_status_200_and_valid_response
```

Run with verbose output:
```bash
uv run pytest -v
```

Run with coverage (requires pytest-cov):
```bash
uv run pytest --cov=src/sdk
```

## Required environment variables
Set these in `.env.local` (preferred) or `.env`.

Authentication and API endpoint:
- `C1_CLIENT_ID`: Your OAuth client ID with access to your org (e.g., `your_client_id@your_domain.com/pcc`).
- `C1_CLIENT_SECRET`: Your OAuth client secret (e.g., `secret-token:conductorone.com:v1:your_secret`).
- `C1_SERVER_URL`: Your API host with protocol (e.g., `https://your-domain.conductor.one`).

Common resource identifiers (used by many tests):
- `C1_APP_ID`: App ID used by app-scoped tests.
- `C1_APP_RESOURCE_TYPE_ID`: Resource type ID under the app.
- `C1_APP_RESOURCE_ID`: Resource ID of an app resource.
- `C1_APP_ENTITLEMENT_ID`: Entitlement ID within the app.
- `C1_IDENTITY_USER_ID`: Identity user ID relevant to entitlement/user-binding tests.

Cross-app proxy tests:
- `C1_APP_ID`: Source app ID (also used as the main app ID for other tests).
- `C1_APP_ENTITLEMENT_ID`: Source app entitlement ID.
- `C1_DST_APP_ID`: Destination app ID.
- `C1_DST_APP_ENTITLEMENT_ID`: Destination app entitlement ID.

Optional for app access requests:
- `C1_REQUEST_POLICY_ID`: Policy ID used to configure defaults.
- `C1_CATALOG_ID`: Request catalog ID used to configure defaults.

Optional for test configuration:
- `C1_TEST_TIMEOUT`: Test timeout in seconds (default: 30).
- `C1_TEST_PAGE_SIZE`: Default page size for tests (default: 10).

## Preconditions / data expectations
- App/resource tests: IDs must belong to the same org and tenant as your credentials.
- Entitlements: `C1_APP_ENTITLEMENT_ID` must exist under `C1_APP_ID`.
- App users: Listing requires a valid `C1_APP_ID` that has app users.
- App resource owners: `C1_APP_RESOURCE_TYPE_ID` and `C1_APP_RESOURCE_ID` must identify an existing resource in `C1_APP_ID`.
- App access requests defaults:
  - GET will return 404 if no defaults exist for `C1_APP_ID`.
  - To exercise create/get/cancel, provide `C1_APP_ID` and supporting IDs (e.g., `C1_APP_RESOURCE_TYPE_ID`, `C1_REQUEST_POLICY_ID`, `C1_CATALOG_ID`). Some backends apply changes asynchronously; a small retry may be necessary before GET returns 200.
- Task audit: Must match expected formats and refer to an existing resource; otherwise the API returns 400.

## Skipping tests
Many tests check for required env vars and log a message instead of failing when inputs are missing. To avoid false negatives, either set all needed variables or run only the tests that match your available data.

## Test structure
- `conftest.py` - Test configuration and SDK setup
- `test_app_*.py` - App-related functionality tests
- `test_user*.py` - User-related functionality tests
- `test_task*.py` - Task-related functionality tests
- `test_automation*.py` - Automation-related functionality tests
- `test_policies*.py` - Policy-related functionality tests

## Troubleshooting
- 401/403: Verify credentials and org access for your client.
- 404 on GET-by-ID: The resource may not exist (wrong ID or wrong app).
- 400 validation errors: Ensure IDs conform to expected formats and relationships (e.g., entitlement belongs to app).
- Long-running operations (create/apply): The backend may be asynchronous; add short retries before asserting GET responses.
