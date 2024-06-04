from typing import TYPE_CHECKING

from tortoise import fields, models

from src.common.models.mixins import TimeBasedMixin

if TYPE_CHECKING:
    from src.core.users.models import User


class Message(models.Model, TimeBasedMixin):
    id = fields.IntField(pk=True)
    sender: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User",
        related_name="sender",
        on_delete=fields.CASCADE,
    )
    receiver: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User",
        related_name="receiver",
        on_delete=fields.CASCADE,
    )
    content = fields.TextField(null=False)
    received = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(description="Время создания", auto_now_add=True)

    receiver_id: int
    sender_id: int

    class Meta:
        table = "chats_message"
