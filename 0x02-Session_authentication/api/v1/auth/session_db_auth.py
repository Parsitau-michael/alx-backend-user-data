#!/usr/bin/env python3
"""New Authentication class"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth Definition"""
    def create_session(self, user_id=None):
        """A method that creates a session"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """A method that returns the User ID
        Args:
            -session_id: the session Id associated with the
            user id to be retrieved
        Return:
            - user_id associated with provided session_id
        """
        if session_id is None:
            return None

        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return None

        if self.session_duration <= 0:
            return None

        if (user_sessions[0].created_at
                + timedelta(seconds=self.session_duration))\
                < datetime.now():
            return None

        return user_sessions[0].user_id

    def destroy_session(self, request=None):
        """A method that destroys the UserSession based on session id
        Args:
            -request: Flasks request object
        Returns:
            - A boolean for whether UserSession was destroyed or not
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return False

        try:
            user_sessions[0].remove()
        except Exception:
            return False

        return True
