from fastapi import status

from src.common.schemas import BaseExceptionSchema


class UnsupportedFileTypeError(BaseExceptionSchema):
    message: str = "Неподдерживаемый тип файла."
    reason: str = "unsupported_file_type"
    status: int = status.HTTP_400_BAD_REQUEST


class MediaNotFoundError(BaseExceptionSchema):
    message: str = "Файла не найдет."
    reason: str = "media_not_found"
    status: int = status.HTTP_404_NOT_FOUND
