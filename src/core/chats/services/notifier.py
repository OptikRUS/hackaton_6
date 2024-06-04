from fastapi import WebSocket

from src.core.chats.models import Message
from src.core.chats.schemas.messages import MessageForSend


class NotifyManager:
    def __init__(self, message_model: Message) -> None:
        self.message_model = message_model
        self.connections: dict[int, WebSocket] = {}

    async def connect(self, sender_id: int, websocket: WebSocket):
        await websocket.accept()
        # TODO: если будет желание, то можно подключить Redis
        self.connections[sender_id] = websocket
        await self.send_notifications()

    async def notification_messages(self, sender_id: int):
        connection = self.connections[sender_id]
        new_message_data = await connection.receive_json()
        new_parsed_message = MessageForSend.model_validate(new_message_data)
        await self._save_message(
            sender_id=new_parsed_message.sender_id,
            receiver_id=new_parsed_message.receiver_id,
            message_text=new_parsed_message.message,
        )

    async def _save_message(self, sender_id: int, receiver_id: int, message_text: str) -> Message:
        return await self.message_model.create(
            sender_id=sender_id, receiver_id=receiver_id, content=message_text
        )

    async def send_notifications(self) -> None:
        new_messages = await self.message_model.filter(
            receiver_id__in=self.connections.keys(), received=False
        )
        for message in new_messages:
            await self._send_message(
                message=message.content, connection=self.connections[message.receiver_id]
            )
            message.received = True
            await message.save()

    async def _send_message(self, message: str, connection: WebSocket) -> None:
        await connection.send_text(message)

    def disconnect(self, sender_id: int) -> None:
        del self.connections[sender_id]
