from .sdk import SDK
from .tokensource import Token
import requests 
from requests.adapters import HTTPAdapter

class TokenAuth(HTTPAdapter):
    """A Transport Adapter that handles Token authentication."""

    def __init__(self, token):
        self.token = token
        super().__init__()

    def add_headers(self, request, **kwargs):
        """Add headers to a request before sending."""
        request.headers['Authorization'] = f'Bearer {self.token}'




def SDKWithCredentials(token_url: str, client_id: str, client_secret: str, **kwargs) -> SDK:
    """Instantiates the SDK configuring it with the provided kwargs and an authed client.
    
    Accepts the same kwargs as SDK, but also requires the following:
    token_url: The URL to use to get a token
    client_id: The client ID to use to get a token
    client_secret: The client secret to use to get a token
    """
    client = requests.Session()
    token_instance = Token(client, token_url, client_id, client_secret)
    token = token_instance.get_token()

    # Instantiate the custom Transport Adapter
    auth = TokenAuth(token)

    # Mount it for both http and https usage
    client.mount('http://', auth)
    client.mount('https://', auth)

    return SDK(**kwargs, client=client)