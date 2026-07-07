from typing import Optional

from sqlalchemy.orm import Session

from app.models.ocr_result import OCRResult


class OCRResultRepository:
    """
    Repository class for OCR Result database operations.
    """

    @staticmethod
    def create_ocr_result(
        db: Session,
        ocr_result: OCRResult
    ) -> OCRResult:

        db.add(ocr_result)
        db.commit()
        db.refresh(ocr_result)

        return ocr_result

    @staticmethod
    def get_ocr_result_by_id(
        db: Session,
        ocr_result_id: int
    ) -> Optional[OCRResult]:

        return (
            db.query(OCRResult)
            .filter(
                OCRResult.ocr_result_id == ocr_result_id
            )
            .first()
        )

    @staticmethod
    def get_ocr_result_by_document(
        db: Session,
        document_id: int
    ) -> Optional[OCRResult]:

        return (
            db.query(OCRResult)
            .filter(
                OCRResult.document_id == document_id
            )
            .first()
        )

    @staticmethod
    def update_parser_result(
        db: Session,
        ocr_result: OCRResult,
        extracted_json: dict,
        confidence_score: float
    ) -> OCRResult:
        """
        Update parser output and confidence score.
        """

        ocr_result.extracted_json = extracted_json
        ocr_result.confidence_score = confidence_score

        db.commit()
        db.refresh(ocr_result)

        return ocr_result

    @staticmethod
    def delete_ocr_result(
        db: Session,
        ocr_result: OCRResult
    ) -> None:

        db.delete(ocr_result)
        db.commit()