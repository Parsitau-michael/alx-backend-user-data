#!/usr/bin/env python3
""" This module defines the authentication class
"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """ A method that hashes the password
    """
    return bcrypt.hashpw(password, bcrypt.gensalt())
