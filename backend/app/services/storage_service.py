import os
import uuid
import shutil
from app.dto.storage_dto import StoredFile
import os
from fastapi import UploadFile


class StorageService:
    """
    Handles physical file storage operations.
    """

    BASE_UPLOAD_FOLDER = "uploads/users"

    @staticmethod
    def create_user_directory(user_id: int) -> str:
        """
        Create user upload directory if it does not exist.
        """

        folder_path = os.path.join(
            StorageService.BASE_UPLOAD_FOLDER,
            str(user_id)
        )

        os.makedirs(folder_path, exist_ok=True)

        return folder_path

    @staticmethod
    def generate_unique_filename(
        original_filename: str
    ) -> str:
        """
        Generate a unique filename.
        """

        unique_id = uuid.uuid4().hex

        return f"{unique_id}_{original_filename}"

    @staticmethod
    def save_file(
        file: UploadFile,
        user_id: int
    ) -> tuple[str, str]:
        """
        Save uploaded file.

        Returns:
            stored_filename,
            file_path
        """

        user_folder = StorageService.create_user_directory(
            user_id
        )

        stored_filename = (
            StorageService.generate_unique_filename(
                file.filename
            )
        )

        file_path = os.path.join(
            user_folder,
            stored_filename
        )
        

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_size = os.path.getsize(file_path)

        return StoredFile(
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_path=file_path,
            file_size=file_size,
            mime_type=file.content_type
        )

    @staticmethod
    def delete_file(
        file_path: str
    ) -> bool:
        """
        Delete stored file.
        """

        if os.path.exists(file_path):

            os.remove(file_path)

            return True

        return False