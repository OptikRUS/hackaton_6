from tortoise.queryset import Q

from src.api.schemas.pagination import PaginationInput
from src.core.chats.api.schemas.requests import ChatHistoryRequest
from src.core.chats.models import Message


class ChatHistoryUseCase:
    def __init__(self, messages_model: Message) -> None:
        self.messages_model = messages_model

    async def get_chat_history(
        self,
        search_filters: ChatHistoryRequest,
        pagination: PaginationInput
    ) -> dict:
        chat_history_qs = self.messages_model.all()
        if search_filters:
            filters = list()
            filters.append(Q(**search_filters.model_dump()))
            search_filters.sender_id, search_filters.receiver_id = (
                search_filters.receiver_id, search_filters.sender_id
            )
            filters.append(Q(**search_filters.model_dump()))

            chat_history_qs = self.messages_model.filter(Q(*filters, join_type="OR"))

        messages: list[Message] = (
            await chat_history_qs
            .offset(pagination.offset)
            .limit(pagination.size)
            .order_by("-created_at")
        )
        return {"messages": messages}
