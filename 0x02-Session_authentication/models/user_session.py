#!/usr/bin/env python3
"""New auth system"""

from models.base import Base


class UserSession(Base):
    """UserSession model class definition"""
    def __init__(self, *args: list, **kwargs: dict):
        super().__init__()
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
