#!/usr/bin/env python3
"""Definition of class SessionAuth"""
from api.v1.auth.auth import Auth
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
