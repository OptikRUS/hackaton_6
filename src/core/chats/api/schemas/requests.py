from src.api.schemas.base_schemas import ApiModel


class SendMessageRequest(ApiModel):
    message: str
    receiver_id: int
