from requests import Session
import base64
import json
import time
from urllib.parse import urlparse
from jose import jwt
from jose.utils import base64url_encode
import secrets

class Token:
    assertion_type: str= 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'

    def __init__(self, client: Session, token_url: str, client_id: str, client_secret: str):
        self.client = client
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret

    def getToken(self):
        name, domain, version, secret = self.client_secret.split(':')
        if name != "secret-token":
            raise Exception("not a secret token")
        if domain != "conductorone.com":
            raise Exception("wrong domain")
        if version != "v1":
            raise Exception("incorrect client-secret version")
        jwk = json.loads(base64.b64decode(secret))
        alg = "EdDSA"


        aud = self.token_url
        hostname = urlparse(aud).hostname
        if hostname:
            aud = hostname

        now = int(time.time())
        nonce = secrets.token_bytes(16)
        
        token = jwt.encode({
            "nonce": nonce,
            "iss": self.client_id,
            "sub": self.client_id,
            "aud": aud,
            "exp": now + 120,
            "iat": now,
            "nbf": now - 120
        }, jwk, algorithm=alg)

        body = {
            "client_id": self.client_id,
            "grant_type": 'client_credentials',
            "client_assertion_type": Token.assertion_type,
            "client_assertion": token
        }
        resp = self.client.post(f"{self.token_url}/auth/v1/token", data=body)

        if resp.status_code != 200:
            raise Exception(f"Failed to get token: {resp.status_code}")
        
        return resp.json().get("access_token")