#!/usr/bin/env python3
"""
Defines a hash_password function
"""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    that takes a plaintext password as input
    """
    encode = password.encode()
    salt = bcrypt.gensalt()
    hashed = hashpw(encode, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if the provided password matches the hashed password
    Args:
        hashed_password (bytes): hashed password
        password (str): password in string
    Return:
        bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
