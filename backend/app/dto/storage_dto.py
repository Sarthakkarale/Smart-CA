from dataclasses import dataclass


@dataclass
class StoredFile:
    """
    Represents a file successfully stored on disk.
    """

    original_filename: str
    stored_filename: str
    file_path: str
    file_size: int
    mime_type: str