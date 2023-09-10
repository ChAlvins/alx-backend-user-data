#!/usr/bin/env python3
"""Definition of class SessionAuth"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import List, TypeVar
import uuid


class SessionAuth(Auth):
    """Implement Session Authorization protocol methods"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a Session ID for a user_id
        :param user_id: User ID (string) to associate with the session
        :return: Session ID (string)
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID:
        session_id: Session ID (str) for which to retrieve the User ID.
        return: User ID (str) associated with Session ID, or None if not found
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Retrieve a User instance based on a cookie value
        """
        sesssion_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sesssion_cookie)

        user = User.get(user_id)
        return user

    def destroy_session(self, request=None) -> bool:
        """Deletes a user session"""
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
