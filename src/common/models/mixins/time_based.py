from datetime import datetime

from tortoise import fields


class TimeBasedMixin:
    updated_at: datetime = fields.DatetimeField(description="Время обновления", auto_now=True)
    created_at: datetime = fields.DatetimeField(description="Время создания", auto_now_add=True)
