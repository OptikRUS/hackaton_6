from typing import TYPE_CHECKING

from tortoise import fields, models

from src.common.models.mixins import TimeBasedMixin

if TYPE_CHECKING:
    from src.core.users.models import User


class Media(models.Model, TimeBasedMixin):
    id = fields.IntField(pk=True)
    file_path = fields.CharField(max_length=100)

    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="media", null=True
    )

    class Meta:
        table = "media_files"
