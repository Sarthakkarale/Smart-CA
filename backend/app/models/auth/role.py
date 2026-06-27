from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String(20), unique=True, nullable=False)

    users = relationship("User", back_populates="role")