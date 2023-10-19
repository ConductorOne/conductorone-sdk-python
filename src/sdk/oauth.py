import requests
import base64
import json
import time
from urllib.parse import urlparse
import jwt
import secrets
from jose.utils import base64url_encode
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

ASSERTION_TYPE = 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'
class UnparsableSecret(Exception):
    pass

def with_authorization(client_id: str, client_secret: str, token_url: str = '', **kwargs) -> (str, str):
    """Returns a tuple of (token, error string) depending on whether the token was successfully retrieved.
    It will use the url in the client_id to get the token URL and tenant domain, if not provided. 
    
    For example a client_id of `foo-bar-123@foobar.conductor.one/pcc` would result in:
        token_url: `https://foobar.conductor.one ` derived from client_id
        tenant_domain: foobar derived from client_id
        server_url: `https://foobar.conductor.one` derived from `https://{tenantDomain}.conductor.one`
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

    url = client_id.split('@')[1].split('/')[0]
    # If no tenant_domain is provided, use the first part of the url
    if 'tenant_domain' not in kwargs:
        kwargs['tenant_domain'] = url.split('.')[0]
    if not token_url:
        # If no token_url is provided, use the url in the client_id
        token_url = 'https://' + url

    try:
        token = get_token(client_id, client_secret, token_url)
        return token, None
    except Exception as e:
        return None, f'Failed to obtain OAuth token: {str(e)}'

def parse_secret(secret: str) -> Ed25519PrivateKey:
    jwk_b64 = secret
    jwk_json = base64.urlsafe_b64decode(jwk_b64).decode('utf-8')
    jwk = json.loads(jwk_json)

    if 'd' not in jwk:
        raise ValueError("Invalid secret: not a private key")
        
    if not jwk['kty'] == 'OKP' or not jwk['crv'] == 'Ed25519':
        raise ValueError("Invalid secret: not an Ed25519 key")

    private_bytes = base64.urlsafe_b64decode(jwk['d'] + '==')
    private_key = Ed25519PrivateKey.from_private_bytes(private_bytes)
    return private_key

def get_token(client_id: str, client_secret: str, token_url: str) -> (str, str):
    name, domain, version, secret = client_secret.split(':')
    if name != "secret-token":
        raise ValueError("Invalid client_secret: name is invalid")
    if domain != "conductorone.com":
        raise ValueError("Invalid client_secret: domain is invalid")
    if version != "v1":
        raise ValueError("Invalid client_secret: version is incorrect")

    # Remove any port number from the audience
    aud = token_url
    hostname = urlparse(aud).hostname
    if hostname:
        aud = hostname

    now = int(time.time())
    nonce = secrets.token_bytes(16)
    
    payload = {
        "nonce": base64url_encode(nonce).decode(),
        "iss": client_id,
        "sub": client_id,
        "aud": aud,
        "exp": now + 120,
        "iat": now,
        "nbf": now - 120
    }

    private_key = parse_secret(secret)
    
    alg = "EdDSA"
    token = jwt.encode(payload, private_key, alg)

    body = {
        "client_id": client_id,
        "grant_type": 'client_credentials',
        "client_assertion_type": ASSERTION_TYPE,
        "client_assertion": token
    }

    client = requests.Session()
    resp = client.post(f"{token_url}/auth/v1/token", data=body)
    resp.raise_for_status()
    return resp.json()['access_token']
        