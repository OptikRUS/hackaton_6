from typing import Any, Annotated

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, status

from src.api.schemas.pagination import PaginationInput
from src.common.auth.authorization import CheckAuthorization
from src.common.auth.schemas import UserTokenPayload
from src.core.chats.api.schemas.requests import ChatHistoryRequest
from src.core.chats.models import Message
from src.core.chats.services.notifier import NotifyManager
from src.core.chats.use_cases.get_chat_history import ChatHistoryUseCase
from src.core.chats.api.schemas import responses

router = APIRouter(prefix="/chats", tags=["chats"])
notify_manager = NotifyManager(message_model=Message())


@router.websocket("/{sender_id}")
async def notify_messages(websocket: WebSocket, sender_id: int) -> Any:
    await notify_manager.connect(sender_id=sender_id, websocket=websocket)
    try:
        while len(notify_manager.connections) > 0:
            await notify_manager.notification_messages(sender_id=sender_id)
            await notify_manager.send_notifications()
    except WebSocketDisconnect:
        notify_manager.disconnect(sender_id=sender_id)


@router.get(
    "/history/",
    response_model=responses.ChatHistoryResponse,
    status_code=status.HTTP_200_OK,
)
async def get_exercise_types(
    pagination: Annotated[PaginationInput, Depends()],
    search: Annotated[ChatHistoryRequest, Depends()],
) -> Any:
    use_case = ChatHistoryUseCase(messages_model=Message())
    return await use_case.get_chat_history(search_filters=search, pagination=pagination)


@router.get(
    "/user/",
    response_model=responses.ChatHistoryResponse,
    status_code=status.HTTP_200_OK,
)
async def get_exercise_types(
    pagination: Annotated[PaginationInput, Depends()],
    search: Annotated[ChatHistoryRequest, Depends()],
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())]
) -> Any:
    use_case = ChatHistoryUseCase(messages_model=Message())
    return await use_case.get_chat_history(search_filters=search, pagination=pagination)
