#!/usr/bin/env python3
"""DB module"""
from user import Base, User


class DB:
    """db class"""
    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Create a User object and save it to the database
        args:
        -email (str): user's email address
        -hashed_password (str): password hashed by bcrypt's hashpw
        return:
        -User: The newly created User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user
