from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class UploadRequest(BaseModel):
    """
    Metadata sent along with the uploaded document.
    The actual file is received separately using FastAPI's UploadFile.
    """

    description: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Optional description of the uploaded document"
    )


class UploadResponse(BaseModel):
    """
    Response returned after a successful upload.
    """

    document_id: int
    original_filename: str
    document_type: Optional[str] = None
    processing_status: str
    message: str

    model_config = ConfigDict(from_attributes=True)