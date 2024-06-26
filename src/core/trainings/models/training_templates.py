from tortoise import fields, models


class TrainingTemplate(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=True)
    description = fields.TextField(null=True)
    exercises = fields.ManyToManyField(
        "models.Exercise",
        related_name="exercises",
        through="training_templates_exercises_m2m",
        backward_key="training_template_id",
        forward_key="exercise_id",
    )
    warm_up = fields.ManyToManyField(
        "models.Exercise",
        related_name="warm_up_templates",
        through="training_exercises_m2m_warm_up_templates",
        backward_key="training_id",
        forward_key="exercise_id",
    )
    warm_down = fields.ManyToManyField(
        "models.Exercise",
        related_name="warm_down_templates",
        through="training_exercises_m2m_warm_down_templates",
        backward_key="training_id",
        forward_key="exercise_id",
    )

    class Meta:
        table = "trainings_training_template"
