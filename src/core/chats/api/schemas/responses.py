from datetime import datetime

from src.api.schemas.base_schemas import ApiModel


class MessageResponse(ApiModel):
    content: str | None = None
    receiver_id: int
    sender_id: int
    url: str | None = None
    received: bool
    created_at: datetime


class ChatHistoryResponse(ApiModel):
    messages: list[MessageResponse]
