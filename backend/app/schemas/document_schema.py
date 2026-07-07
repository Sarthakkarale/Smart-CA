from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.core.constants import (
    DocumentType,
    ProcessingStatus
)


class DocumentResponse(BaseModel):
    """
    Document information returned to the frontend.
    """

    document_id: int

    user_id: int

    original_filename: str

    stored_filename: str

    file_path: str

    file_size: int

    mime_type: str

    document_type: Optional[DocumentType] = None

    processing_status: ProcessingStatus

    upload_time: datetime

    processed_time: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)