from tortoise import fields, models
from tortoise.validators import MaxValueValidator, MinValueValidator

from src.common.auth.constants import UserRoles
from src.common.models.mixins import TimeBasedMixin
from src.core.users.constants import GenderType


class User(models.Model, TimeBasedMixin):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, null=False)
    password = fields.CharField(max_length=255, null=False)
    phone = fields.CharField(max_length=15, null=True)
    name = fields.CharField(max_length=255, null=True)
    surname = fields.CharField(max_length=255, null=True)
    patronymic = fields.CharField(max_length=255, null=True)
    gender = fields.data.CharEnumField(enum_type=GenderType, max_length=6, null=True)
    role = fields.data.CharEnumField(
        enum_type=UserRoles, default=UserRoles.CLIENT, max_length=7, null=False
    )
    age = fields.SmallIntField(validators=[MinValueValidator(min_value=18)], null=True)
    weight = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    height = fields.FloatField(validators=[MinValueValidator(min_value=0.0)], null=True)
    rate = fields.FloatField(
        default=0.0,
        validators=[MinValueValidator(min_value=0.0), MaxValueValidator(max_value=5.0)],
        null=True,
    )
    avatar_path = fields.CharField(max_length=355, null=True)

    description = fields.TextField(null=True)
    trainers = fields.ManyToManyField(
        "models.User",
        related_name="client_trainers",
        through="trainers_clients_m2m",
        backward_key="client_id",
        forward_key="trainer_id",
    )
    clients = fields.ManyToManyField(
        "models.User",
        related_name="trainer_clients",
        through="trainers_clients_m2m",
        backward_key="trainer_id",
        forward_key="client_id",
    )
    trainings = fields.ManyToManyField(
        "models.Training",
        through="trainings_trainers_m2m",
        backward_key="user_id",
    )

    @property
    def full_name(self) -> str:
        full_name = ""
        if self.surname:
            full_name += self.surname
        if self.name:
            full_name += self.name
        if self.patronymic:
            full_name += self.patronymic
        return full_name

    class Meta:
        table = "users_user"
