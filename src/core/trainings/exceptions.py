from fastapi import status

from src.common.schemas import BaseExceptionSchema


class TrainingNotFoundError(BaseExceptionSchema):
    message: str = "Тренировка не найдена."
    reason: str = "training_not_found"
    status: int = status.HTTP_404_NOT_FOUND


class TrainingAlreadyExistsError(BaseExceptionSchema):
    message: str = "Тренировка уже существует."
    reason: str = "training_already_exists"
    status: int = status.HTTP_409_CONFLICT


class TrainingTypeNotFoundError(BaseExceptionSchema):
    message: str = "Тип тренировки не найден."
    reason: str = "training_type_not_found"
    status: int = status.HTTP_404_NOT_FOUND


class IncorrectTrainingTimeError(BaseExceptionSchema):
    message: str = "Некорректное время тренировки."
    reason: str = "incorrect_training_time_error"
    status: int = status.HTTP_400_BAD_REQUEST
