from tortoise import fields, models


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
    trainings = fields.ManyToManyField(
        "models.Training",
        related_name="trainings",
        through="trainings_exercises_m2m",
        backward_key="exercise_id",
    )

    class Meta:
        table = "trainings_exercise"


class ExercisePhoto(models.Model):
    id = fields.IntField(pk=True)
    exercise: fields.ForeignKeyRelation["Exercise"] = fields.ForeignKeyField(
        "models.Exercise", related_name="photos"
    )

    class Meta:
        table = "trainings_exercise_photo"
