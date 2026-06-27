from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean, ForeignKey
from sqlalchemy.sql import func

from app.db.database import Base


class UserSession(Base):
    __tablename__ = "user_sessions"

    session_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    refresh_token = Column(Text, nullable=False)

    ip_address = Column(String(100))

    user_agent = Column(Text)

    expires_at = Column(DateTime)

    is_revoked = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())