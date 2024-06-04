from fastapi import status

from src.common.exceptions import BaseHTTPException


class InvalidTokenException(BaseHTTPException):
    status: int = status.HTTP_401_UNAUTHORIZED
    reason: str = "user_unauthorized"
    message: str | None = "Пользователь не авторизован."


class AccessDeniedException(BaseHTTPException):
    status: int = status.HTTP_403_FORBIDDEN
    reason: str = "forbidden"
    message: str | None = "Пользователь не имеет доступа к ресурсу."
