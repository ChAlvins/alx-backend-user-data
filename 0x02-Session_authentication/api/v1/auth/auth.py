#!/usr/bin/env python3
"""class Auth """
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Manages the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
         Check if authentication is required for the given path.
         Returns True if path is None or excluded_paths is None/empty.
         Returns False if path is in excluded_paths.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] is not '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Placeholder method for retrieving authorization header.
        Returns None for now
        """
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for getting the current user.
        Returns None for now.
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request
        :param request: Flask request object
        :return: Value of the session cookie, or None if not found
        method retrieves name of the session cookie from the environment
        variable SESSION_NAME. By default, it's set to "_my_session_id"
        """
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_name)
