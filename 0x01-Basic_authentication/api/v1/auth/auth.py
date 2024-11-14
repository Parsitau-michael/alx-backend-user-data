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
        if not excluded_paths or path is None:
            return True
        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        # If no match is found in excluded_paths, return True
        return True

    def authorization_header(self, request=None) -> str:
        """ A method that returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ A method that returns None
        """
        return None
