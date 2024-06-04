from pydantic import Field

from src.api.schemas.base_schemas import BaseDTO


class MessageForSend(BaseDTO):
    message: str = Field(alias="content")
    receiver_id: int
    sender_id: int
