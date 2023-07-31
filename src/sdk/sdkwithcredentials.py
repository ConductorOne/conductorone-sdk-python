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




def SDKWithCredentials(token_url: str, client_id: str, client_secret: str):
    client = requests.Session()
    token_instance = Token(client, token_url, client_id, client_secret)
    token = token_instance.getToken()

    # Instantiate the custom Transport Adapter
    auth = TokenAuth(token)

    # Mount it for both http and https usage
    client.mount('http://', auth)
    client.mount('https://', auth)

    return SDK(client=client)