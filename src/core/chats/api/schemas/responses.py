from datetime import datetime

from pydantic import Field

from src.api.schemas.base_schemas import ApiModel


class MessageResponse(ApiModel):
    content: str | None = Field(alias="message")
    receiver_id: int
    sender_id: int
    url: str | None = None
    received: bool
    created_at: datetime


class ChatHistoryResponse(ApiModel):
    messages: list[MessageResponse]
