#!/usr/bin/env python3
""" This module represents a Auth class
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ This class is the template for all authentication
    system I will implement.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ A method that checks whether authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ A method that returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ A method that returns None
        """
        return None
