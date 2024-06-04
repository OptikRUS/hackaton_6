from typing import Any

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.core.chats.models import Message
from src.core.chats.services.notifier import NotifyManager

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
