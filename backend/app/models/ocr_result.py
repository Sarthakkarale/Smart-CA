from sqlalchemy import (
    Column,
    Integer,
    Text,
    JSON,
    Float,
    DateTime,
    Enum,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base
from app.core.constants import (
    OCREngine,
    ParserEngine
)


class OCRResult(Base):
    __tablename__ = "ocr_results"

    # -------------------------
    # Primary Key
    # -------------------------
    ocr_result_id = Column(
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
    # OCR Output
    # -------------------------
    raw_text = Column(
        Text,
        nullable=False
    )

    # -------------------------
    # AI Parsed JSON
    # -------------------------
    extracted_json = Column(
        JSON,
        nullable=True
    )

    # -------------------------
    # Confidence Score
    # -------------------------
    confidence_score = Column(
        Float,
        nullable=True
    )

    # -------------------------
    # Engines Used
    # -------------------------
    ocr_engine = Column(
        Enum(OCREngine),
        nullable=False
    )

    parser_engine = Column(
        Enum(ParserEngine),
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
        back_populates="ocr_results"
    )