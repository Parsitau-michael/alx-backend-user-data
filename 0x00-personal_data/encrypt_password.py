#!/usr/bin/env python3
"""A module that implements a hash_password function"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    A function to hash a password
    Args:
        password - a string representing user password
    Returns - a salted, hashed password which is a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    A function that validates provided password against the hashed one
    Args:
        hashed_password: the hashed password in bytes
        password: provided password(str)
    Returns: A boolean confirming whether the passwords match
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
