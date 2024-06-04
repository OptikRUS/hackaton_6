from pydantic import Field

from src.api.schemas.base_schemas import BaseErrorSchema


class ReceiverNotFoundErrorSchema(BaseErrorSchema):
    message: str | None = Field(
        None,
        json_schema_extra={"example": "Получатель не найден."},
    )
    reason: str | None = Field(None, json_schema_extra={"example": "receiver_not_found"})
