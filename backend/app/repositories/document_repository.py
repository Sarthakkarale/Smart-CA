from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.document import Document
from app.core.constants import (
    ProcessingStatus,
    DocumentType
)


class DocumentRepository:
    """
    Repository class for Document database operations.
    """

    @staticmethod
    def create_document(
        db: Session,
        document: Document
    ) -> Document:
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def get_document_by_id(
        db: Session,
        document_id: int
    ) -> Optional[Document]:
        return (
            db.query(Document)
            .filter(Document.document_id == document_id)
            .first()
        )

    @staticmethod
    def get_documents_by_user(
        db: Session,
        user_id: int
    ) -> List[Document]:
        return (
            db.query(Document)
            .filter(Document.user_id == user_id)
            .order_by(Document.upload_time.desc())
            .all()
        )

    @staticmethod
    def update_document_status(
        db: Session,
        document: Document,
        status: ProcessingStatus
    ) -> Document:

        document.processing_status = status

        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def update_document_type(
        db: Session,
        document: Document,
        document_type: DocumentType
    ) -> Document:

        document.document_type = document_type

        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def update_processed_time(
        db: Session,
        document: Document
    ) -> Document:

        from sqlalchemy.sql import func

        document.processed_time = func.now()

        db.commit()
        db.refresh(document)

        return document

    @staticmethod
    def delete_document(
        db: Session,
        document: Document
    ) -> None:

        db.delete(document)
        db.commit()