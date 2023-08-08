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




def SDKWithCredentials(client_id: str, client_secret: str, token_url: str = '', **kwargs) -> SDK:
    """Instantiates the SDK configuring it with the provided kwargs and an authed client.
    It will use the url in the client_id to get the token URL and tenant domain, if not provided. 
    
    For example a client_id of foo-bar-123@foobar.conductor.one/pcc would result in:
    token_url: https://foobar.conductor.one 
    tenant_domain: foobar 
    server_url: https://foobar.conductor.one [https://{tenantDomain}.conductor.one]
    If this is not the case, you can provide the token_url and tenant_domain/server_url in the kwargs.

    :param client_id: The client ID to use to get a token
    :type client_id: str
    :param client_secret: The client secret to use to get a token
    :type client_secret: str
    :param token_url: The URL to use to get a token (if not provided, will be derived from client_id)
    :type token_url: str
    :param kwargs: Additional arguments to pass to the SDK constructor
    :type kwargs: dict[str, any]
    """
    client = requests.Session()

    url = client_id.split('@')[1].split('/')[0]
    # If no tenant_domain is provided, use the first part of the url
    if 'tenant_domain' not in kwargs:
        kwargs['tenant_domain'] = url.split('.')[0]
    if not token_url:
        # If no token_url is provided, use the url in the client_id
        token_url = 'https://' + url

    token_instance = Token(client, token_url, client_id, client_secret)
    token = token_instance.get_token()

    # Instantiate the custom Transport Adapter
    auth = TokenAuth(token)

    # Mount it for https usage
    client.mount('https://', auth)

    return SDK(client=client, **kwargs)