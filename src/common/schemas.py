from fastapi import status

from src.common.exceptions import BaseHTTPException


class BaseExceptionSchema(BaseHTTPException):
    message: str = "Сообщение об ошибке."
    reason: str = "error_reason"
    status: int = status.HTTP_400_BAD_REQUEST
