from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    Enum,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base
from app.core.constants import (
    LogStage,
    LogStatus
)


class DocumentLog(Base):
    __tablename__ = "document_logs"

    # -------------------------
    # Primary Key
    # -------------------------
    log_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    # -------------------------
    # Foreign Key
    # -------------------------
    document_id = Column(
        Integer,
        ForeignKey("documents.document_id"),
        nullable=False
    )

    # -------------------------
    # Processing Stage
    # -------------------------
    stage = Column(
        Enum(LogStage),
        nullable=False
    )

    # -------------------------
    # Status
    # -------------------------
    status = Column(
        Enum(LogStatus),
        nullable=False
    )

    # -------------------------
    # Log Message
    # -------------------------
    message = Column(
        Text,
        nullable=True
    )

    # -------------------------
    # Timestamp
    # -------------------------
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # -------------------------
    # Relationship
    # -------------------------
    document = relationship(
        "Document",
        back_populates="logs"
    )