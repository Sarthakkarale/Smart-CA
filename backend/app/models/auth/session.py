from sqlalchemy import Column, Integer, Text, DateTime, Boolean, ForeignKey, String
from sqlalchemy.sql import func

from app.db.database import Base


class UserSession(Base):
    __tablename__ = "user_sessions"

    session_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    refresh_token = Column(Text)

    ip_address = Column(String(100))

    user_agent = Column(Text)

    device_name = Column(String(150))

    expires_at = Column(DateTime)

    last_used_at = Column(DateTime)

    is_revoked = Column(Boolean, default=False)

    created_at = Column(DateTime, server_default=func.now())