from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.core.constants import OCREngine


class OCRResultResponse(BaseModel):
    """
    OCR extraction result before AI parsing.
    """

    ocr_result_id: int

    document_id: int

    raw_text: str

    confidence_score: Optional[float] = None

    ocr_engine: OCREngine

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)