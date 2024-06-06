from pydantic import EmailStr

from src.api.schemas.base_schemas import ApiModel
from src.common.auth.constants import UserRoles
from src.core.users.constants import GenderType


class UserResponse(ApiModel):
    id: int
    email: EmailStr
    phone: str | None
    name: str | None
    surname: str | None
    patronymic: str | None
    gender: GenderType | None
    role: UserRoles
    age: int | None
    weight: float | None
    height: float | None
    rate: float | None
    description: str | None


class TrainerResponse(ApiModel):
    id: int
    surname: str
    name: str
    patronymic: str
    gender: str
    age: int
    rate: float


class TrainerListResponse(ApiModel):
    result: list[TrainerResponse]


class UnBindTrainerRequest(ApiModel):
    trainer_id: int


class UnBindTrainerResponse(ApiModel):
    trainer_id: int
    client_id: int
