#!/usr/bin/env python3
""" This module defines BasicAuth a subclass of Auth
"""


from models.user import User
from api.v1.auth.auth import Auth
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """ This is a class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None:
            return None

        if isinstance(authorization_header, str):
            if authorization_header.startswith("Basic "):
                return authorization_header[6:]

        return None

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """ returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header,
                                             validate=True)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, TypeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ A method that that returns the user email and password from
        the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """ A method that returns the user instance based on his
        email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({"email": user_email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
