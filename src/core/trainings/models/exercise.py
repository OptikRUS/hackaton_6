from tortoise import fields, models
from tortoise.validators import MinValueValidator


class Exercise(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    muscle = fields.CharField(max_length=255, null=True)
    additional_muscle = fields.CharField(max_length=255, null=True)
    # TODO: добавить Enum
    exercise_type = fields.CharField(max_length=255, null=True)
    equipment = fields.CharField(max_length=255, null=True)
    # TODO: добавить Enum
    difficulty = fields.CharField(max_length=255, null=True)

    distance = fields.FloatField(
        default=None,
        validators=[MinValueValidator(min_value=0.0)],
        null=True,
    )
    count = fields.SmallIntField(validators=[MinValueValidator(min_value=0)], null=True)
    frequency = fields.SmallIntField(validators=[MinValueValidator(min_value=0)], null=True)
    weight = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    height = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    duration = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    length = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)

    class Meta:
        table = "trainings_exercise"


class ExercisePhoto(models.Model):
    id = fields.IntField(pk=True)
    file_path = fields.CharField(max_length=255, null=False)
    exercise: fields.ForeignKeyRelation["Exercise"] = fields.ForeignKeyField(
        "models.Exercise", related_name="photos"
    )

    class Meta:
        table = "trainings_exercise_photo"
