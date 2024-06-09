from typing import TYPE_CHECKING

from tortoise import fields, models
from tortoise.validators import MinValueValidator

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

    count = fields.SmallIntField(validators=[MinValueValidator(min_value=18)], null=True)
    frequency = fields.SmallIntField(validators=[MinValueValidator(min_value=18)], null=True)
    weight = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    height = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    duration = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    length = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    description = fields.TextField(null=True)
    training: fields.ForeignKeyRelation["Training"] = fields.ForeignKeyField(
        "models.Training", related_name="exercises", on_delete=fields.SET_NULL, null=True
    )
    exercise: fields.ForeignKeyRelation["Exercise"] = fields.ForeignKeyField(
        "models.Exercise", related_name="exercise", on_delete=fields.SET_NULL, null=True
    )

    class Meta:
        table = "trainings_training_exercise"
