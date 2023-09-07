#!/usr/bin/env python3
"""For BasicAuth class"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Implement Basic Authorization protocol methods"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for a Basic
        Authorization
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[-1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode and return the value of a Base64 string as a UTF-8 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.b64decode(base64_authorization_header)
            return decoded_value.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract and return the user email and password from
        a decoded Base64 authorization header
        returns a tuple with two values: (email, password)
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)
