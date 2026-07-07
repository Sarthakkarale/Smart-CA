from sqlalchemy.orm import Session
from fastapi import UploadFile

from app.models.document import Document
from app.models.document_log import DocumentLog

from app.repositories.document_repository import DocumentRepository
from app.repositories.document_log_repository import DocumentLogRepository

from app.services.storage_service import StorageService

from app.core.constants import (
    ProcessingStatus,
    LogStage,
    LogStatus
)


class UploadService:
    """
    Handles document upload workflow.
    """

    @staticmethod
    def upload_document(
        db: Session,
        user_id: int,
        file: UploadFile
    ) -> Document:

        # Save file
        stored_file = StorageService.save_file(
        file=file,
        user_id=user_id
        )

        # Create Document model
        document = Document(
            user_id=user_id,
            original_filename=stored_file.original_filename,
            stored_filename=stored_file.stored_filename,
            file_path=stored_file.file_path,
            file_size=stored_file.file_size,
            mime_type=stored_file.mime_type,
            processing_status=ProcessingStatus.UPLOADED
        )

        # Save document
        document = DocumentRepository.create_document(
            db,
            document
        )

        # Create upload log
        log = DocumentLog(
            document_id=document.document_id,
            stage=LogStage.FILE_UPLOAD,
            status=LogStatus.SUCCESS,
            message="Document uploaded successfully."
        )

        DocumentLogRepository.create_log(
            db,
            log
        )

        return document