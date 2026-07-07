from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict

from app.core.constants import (
    DocumentType,
    ParserEngine
)


class ParserResultResponse(BaseModel):
    """
    Structured data returned by the AI parser (Ollama).
    """

    document_type: DocumentType

    parser_engine: ParserEngine

    extracted_data: Dict[str, Any]

    confidence_score: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)