from tortoise.queryset import Q

from src.api.schemas.pagination import PaginationInput
from src.core.chats.api.schemas.requests import ChatHistoryRequest
from src.core.chats.models import Message


class ChatHistoryUseCase:
    def __init__(self, messages_model: Message) -> None:
        self.messages_model = messages_model

    async def get_chat_history(
        self,
        user_id: int,
        search_filters: ChatHistoryRequest,
        pagination: PaginationInput
    ) -> dict:
        chat_history_qs = self.messages_model.all()
        if search_filters:
            filters = list()
            filters.append(Q(
                sender_id=user_id,
                receiver_id=search_filters.receiver_id
            ))
            filters.append(Q(
                receiver_id=user_id,
                sender_id=search_filters.receiver_id
            ))
            chat_history_qs = self.messages_model.filter(
                Q(*filters, join_type="OR")
            )

        messages: list[Message] = (
            await chat_history_qs
            .offset(pagination.offset)
            .limit(pagination.size)
            .order_by("-created_at")
        )
        return {"messages": messages}
