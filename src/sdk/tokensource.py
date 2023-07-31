import requests
import base64
import json
import time
from urllib.parse import urlparse
import jwt
import secrets
from jose.utils import base64url_encode
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.exceptions import *



class Token:
    assertion_type: str= 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'

    def __init__(self, client: requests.Session, token_url: str, client_id: str, client_secret: str):
        self.client = client
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret

    def _parse_secret(secret: str):
        jwk_b64 = secret
        jwk_json = base64.urlsafe_b64decode(jwk_b64 + '==').decode('utf-8')
        jwk = json.loads(jwk_json)

        if 'd' not in jwk:
            raise ValueError("Invalid client secret: not a private key")
            
        if not jwk['kty'] == 'OKP' or not jwk['crv'] == 'Ed25519':
            raise ValueError("Invalid client secret: not an Ed25519 key")

        private_bytes = base64.urlsafe_b64decode(jwk['d'] + '==')
        try:
            private_key = Ed25519PrivateKey.from_private_bytes(private_bytes)
        except UnsupportedAlgorithm:
            print("Unsupported algorithm. Make sure that the key type and curve are correct.")
            raise
        except ValueError:
            print("Invalid key bytes. Make sure that the key bytes are correct.")
            raise

        return private_key

    def getToken(self):
        name, domain, version, secret = self.client_secret.split(':')
        if name != "secret-token":
            raise Exception("not a secret token")
        if domain != "conductorone.com":
            raise Exception("wrong domain")
        if version != "v1":
            raise Exception("incorrect client-secret version")

        aud = self.token_url
        hostname = urlparse(aud).hostname
        if hostname:
            aud = hostname

        now = int(time.time())
        nonce = secrets.token_bytes(16)
        
        payload = {
            "nonce": base64url_encode(nonce).decode(),
            "iss": self.client_id,
            "sub": self.client_id,
            "aud": aud,
            "exp": now + 120,
            "iat": now,
            "nbf": now - 120
        }
        pk = Token._parse_secret(secret)
        alg = "EdDSA"
        token = jwt.encode(payload, pk, alg)

        body = {
            "client_id": self.client_id,
            "grant_type": 'client_credentials',
            "client_assertion_type": Token.assertion_type,
            "client_assertion": token
        }
        resp = self.client.post(f"{self.token_url}auth/v1/token", data=body)

        if resp.status_code != 200:
            raise Exception(f"Failed to get token: {resp.status_code}")
        return resp.json().get("access_token")