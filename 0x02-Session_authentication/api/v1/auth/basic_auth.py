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
        except (ValueError, UnicodeDecodeError):
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
        if not isinstance(users, list) or len(users) == 0:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ A method that overloads Auth and retrieves the User
        instance for a request
        """
        # Step 1: Retrieve the Authorization header
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        # Step 2: Extract the Base64 encoded part of the Authorization header
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if not base64_auth:
            return None

        # Step 3: Decode the Base64 encoded part to a string
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if not decoded_auth:
            return None

        # Step 4: Extract user credentials (email and password)
        user_email, user_pasword = self.extract_user_credentials(decoded_auth)
        if not user_email or not user_pasword:
            return None

        # Step 5: Retrieve the User object using the credentials
        user = self.user_object_from_credentials(user_email, user_pasword)
        return user
