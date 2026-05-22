#!/usr/bin/env python3

"""
Define a function hash_passwprd
Import bcrypt
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with a salt using bcrypt.
    Args:
        password (str): The password to hash.
    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check if password is valid
    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to validate
        """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
