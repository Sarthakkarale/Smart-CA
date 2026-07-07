from enum import Enum


class ProcessingStatus(str, Enum):
    """
    OCR document processing status.
    """

    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class DocumentType(str, Enum):
    """
    Supported document types.
    """

    PAN_CARD = "PAN_CARD"
    AADHAAR_CARD = "AADHAAR_CARD"
    FORM_16 = "FORM_16"
    SALARY_SLIP = "SALARY_SLIP"
    BANK_STATEMENT = "BANK_STATEMENT"
    GST_INVOICE = "GST_INVOICE"
    RENT_RECEIPT = "RENT_RECEIPT"
    INSURANCE_POLICY = "INSURANCE_POLICY"
    MUTUAL_FUND_STATEMENT = "MUTUAL_FUND_STATEMENT"
    LOAN_STATEMENT = "LOAN_STATEMENT"
    OTHER = "OTHER"


class SupportedFileType(str, Enum):
    """
    Allowed upload file extensions.
    """

    PDF = "pdf"
    JPG = "jpg"
    JPEG = "jpeg"
    PNG = "png"


class OCREngine(str, Enum):
    """
    Supported OCR engines.
    """

    PADDLE_OCR = "PaddleOCR"
    TESSERACT = "Tesseract"


class ParserEngine(str, Enum):
    """
    Supported AI parsers.
    """

    OLLAMA = "Ollama"
    QWEN = "Qwen2.5"
    GEMINI = "Gemini"
    GPT = "OpenAI"


class LogStage(str, Enum):
    """
    OCR processing stages.
    """

    FILE_UPLOAD = "FILE_UPLOAD"
    PDF_CONVERSION = "PDF_CONVERSION"
    IMAGE_PREPROCESSING = "IMAGE_PREPROCESSING"
    OCR = "OCR"
    DOCUMENT_CLASSIFICATION = "DOCUMENT_CLASSIFICATION"
    AI_PARSING = "AI_PARSING"
    VALIDATION = "VALIDATION"
    DATABASE_SAVE = "DATABASE_SAVE"


class LogStatus(str, Enum):
    """
    Status of each processing stage.
    """

    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    WARNING = "WARNING"