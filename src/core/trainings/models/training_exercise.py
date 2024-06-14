from typing import TYPE_CHECKING

from tortoise import fields, models
from tortoise.validators import MinValueValidator

from src.core.trainings.constants import IntensityType

if TYPE_CHECKING:
    from src.core.trainings.models.exercise import Exercise
    from src.core.trainings.models.training import Training


class TrainingExercise(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=True)
    distance = fields.FloatField(
        default=0.0,
        validators=[MinValueValidator(min_value=0.0)],
        null=True,
    )
    duration = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    set_count = fields.SmallIntField(validators=[MinValueValidator(min_value=0)], null=True)
    rep_count = fields.SmallIntField(validators=[MinValueValidator(min_value=0)], null=True)
    weight_used = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    rest_period = fields.SmallIntField(validators=[MinValueValidator(min_value=0)], null=True)
    intensity = fields.data.CharEnumField(enum_type=IntensityType, null=False)

    description = fields.TextField(null=True)
    training: fields.ForeignKeyRelation["Training"] = fields.ForeignKeyField(
        "models.Training", related_name="exercises", on_delete=fields.SET_NULL, null=True
    )
    exercise: fields.ForeignKeyRelation["Exercise"] = fields.ForeignKeyField(
        "models.Exercise", related_name="exercise", on_delete=fields.SET_NULL, null=True
    )

    class Meta:
        table = "trainings_training_exercise"
