#!/usr/bin/env python3
""" This module defines BasicAuth a subclass of Auth
"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ This is a class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if authorization_header is None:
            return None
        
        if isinstance(authorization_header, str):
            if authorization_header.startswith("Basic "):
                return authorization_header[6:]

        return None
