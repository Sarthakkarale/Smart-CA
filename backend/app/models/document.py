from sqlalchemy import (
    Column,
    Integer,
    String,
    BigInteger,
    DateTime,
    Enum,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base
from app.core.constants import (
    ProcessingStatus,
    DocumentType
)


class Document(Base):
    __tablename__ = "documents"

    # -------------------------
    # Primary Key
    # -------------------------
    document_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    # -------------------------
    # Foreign Key
    # -------------------------
    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )

    # -------------------------
    # File Information
    # -------------------------
    original_filename = Column(
        String(255),
        nullable=False
    )

    stored_filename = Column(
        String(255),
        unique=True,
        nullable=False
    )

    file_path = Column(
        String(500),
        nullable=False
    )

    file_size = Column(
        BigInteger,
        nullable=False
    )

    mime_type = Column(
        String(100),
        nullable=False
    )

    # -------------------------
    # Document Details
    # -------------------------
    document_type = Column(
        Enum(DocumentType),
        nullable=True
    )

    processing_status = Column(
        Enum(ProcessingStatus),
        default=ProcessingStatus.UPLOADED,
        nullable=False
    )

    # -------------------------
    # Timestamps
    # -------------------------
    upload_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    processed_time = Column(
        DateTime(timezone=True),
        nullable=True
    )

    # -------------------------
    # Relationships
    # -------------------------
    user = relationship(
        "User",
        back_populates="documents"
    )

    ocr_results = relationship(
        "OCRResult",
        back_populates="document",
        cascade="all, delete-orphan"
    )

    logs = relationship(
        "DocumentLog",
        back_populates="document",
        cascade="all, delete-orphan"
    )