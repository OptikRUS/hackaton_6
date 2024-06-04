from fastapi import status

from src.common.schemas import BaseExceptionSchema


class UserAlreadyExistsError(BaseExceptionSchema):
    message: str = "Пользователь уже существует."
    reason: str = "user_already_exists"
    status: int = status.HTTP_400_BAD_REQUEST


class UserNotFoundError(BaseExceptionSchema):
    message: str = "Пользователь не найден."
    reason: str = "brand_not_found"


class IncorrectCredentials(BaseExceptionSchema):
    message: str = "Неверный логин или пароль."
    reason: str = "incorrect_credentials"
