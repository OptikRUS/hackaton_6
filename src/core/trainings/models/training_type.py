from tortoise import fields, models


class TrainingType(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=True)
    description = fields.TextField(null=True)

    class Meta:
        table = "trainings_training_type"
