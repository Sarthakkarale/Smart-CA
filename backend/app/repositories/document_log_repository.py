from typing import List

from sqlalchemy.orm import Session

from app.models.document_log import DocumentLog


class DocumentLogRepository:
    """
    Repository class for document processing logs.
    """

    @staticmethod
    def create_log(
        db: Session,
        log: DocumentLog
    ) -> DocumentLog:

        db.add(log)
        db.commit()
        db.refresh(log)

        return log

    @staticmethod
    def get_logs_by_document(
        db: Session,
        document_id: int
    ) -> List[DocumentLog]:

        return (
            db.query(DocumentLog)
            .filter(
                DocumentLog.document_id == document_id
            )
            .order_by(DocumentLog.created_at.asc())
            .all()
        )

    @staticmethod
    def delete_logs_by_document(
        db: Session,
        document_id: int
    ) -> None:

        (
            db.query(DocumentLog)
            .filter(
                DocumentLog.document_id == document_id
            )
            .delete()
        )

        db.commit()