import os
import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Load environment variables
from dotenv import load_dotenv

# Load .env files in order of precedence
env_files = [".env.local", ".env"]
for env_file in env_files:
    env_path = Path(__file__).parent.parent / env_file
    if env_path.exists():
        load_dotenv(env_path, override=True)

print('Running setup for ConductorOne SDK Python tests...')

# Ensure environment variables are set
required_vars = ['C1_CLIENT_ID', 'C1_CLIENT_SECRET', 'C1_SERVER_URL']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    raise ValueError(f'Missing required environment variables: {", ".join(missing_vars)}')

# Import and initialize SDK
import sdk
from sdk.models import shared

# Create SDK instance
sdk_instance = sdk.sdk_with_credentials(
    client_id=os.getenv('C1_CLIENT_ID') or '',
    client_secret=os.getenv('C1_CLIENT_SECRET') or '',
    server_url=os.getenv('C1_SERVER_URL') or '',
)

# Export for use in tests
__all__ = ['sdk_instance', 'sdk', 'shared']
