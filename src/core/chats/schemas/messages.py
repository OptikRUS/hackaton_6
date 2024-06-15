from pydantic import Field

from src.api.schemas.base_schemas import BaseDTO


class MessageForSend(BaseDTO):
    message: str | None = None
    receiver_id: int
    sender_id: int
    file_path: str | None = None
