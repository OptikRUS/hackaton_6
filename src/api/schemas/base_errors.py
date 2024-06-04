from src.api.schemas.base_schemas import ApiModel


class ErrorSchema(ApiModel):
    message: str | None
    reason: str | None


class ServerError(ErrorSchema):
    message: str = "Ошибка сервера"
    reason: str = "Временные технические неполадки"


class BadRequestError(ErrorSchema):
    message: str = "Запрос не может быть обработан"
    reason: str = "Запрос является некорректным"
