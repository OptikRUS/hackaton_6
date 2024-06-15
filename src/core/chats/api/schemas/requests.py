from src.api.schemas.base_schemas import ApiModel


class ChatHistoryRequest(ApiModel):
    receiver_id: int
