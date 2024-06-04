from typing import TYPE_CHECKING

from tortoise import fields, models

from src.common.auth.constants import UserRoles

if TYPE_CHECKING:
    from src.core.trainings.models.training_type import TrainingType


class Training(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=True)
    training_type: fields.ForeignKeyRelation["TrainingType"] = fields.ForeignKeyField(
        "models.TrainingType", related_name="training", on_delete=fields.SET_NULL, null=True
    )
    description = fields.TextField(null=True)
    date_of_training = fields.DateField(null=True)
    start_time_of_training = fields.TimeField(null=True)
    end_time_of_training = fields.TimeField(null=True)
    appointed_by = fields.data.CharEnumField(
        enum_type=UserRoles, default=UserRoles.CLIENT, max_length=7, null=True
    )
    confirm_by_trainer = fields.BooleanField(default=False)
    past = fields.BooleanField(default=False)

    @property
    def weekday_of_training(self) -> int:
        return self.date_of_training.weekday()

    @property
    def ru_weekday_of_training(self) -> str:
        return self.weekdays_dict[self.weekday_of_training]

    @property
    def weekdays_dict(self) -> dict:
        return {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье",
        }

    class Meta:
        table = "trainings_training"
