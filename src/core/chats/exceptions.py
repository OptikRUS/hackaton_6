from fastapi import status

from src.common.schemas import BaseExceptionSchema


class ReceiverNotFoundError(BaseExceptionSchema):
    message: str = "Получатель не найден."
    reason: str = "receiver_not_found"
    status: int = status.HTTP_404_NOT_FOUND
