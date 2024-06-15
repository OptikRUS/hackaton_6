from src.api.schemas.base_schemas import ApiModel


class ChatHistoryRequest(ApiModel):
    sender_id: int
    receiver_id: int
