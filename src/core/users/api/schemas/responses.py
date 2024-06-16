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
    url: str | None


class TrainerResponse(ApiModel):
    id: int
    surname: str | None
    name: str | None
    patronymic: str | None
    email: str | None
    gender: str | None
    age: int | None
    rate: float | None
    url: str | None


class TrainerListResponse(ApiModel):
    result: list[TrainerResponse]


class ClientResponse(TrainerResponse): ...


class ClientListResponse(ApiModel):
    result: list[ClientResponse]


class UnBindTrainerRequest(ApiModel):
    trainer_id: int


class UnBindTrainerResponse(ApiModel):
    trainer_id: int
    client_id: int


class MediaResponse(ApiModel):
    id: int
    user_id: int
    url: str


class UserMediaResponse(ApiModel):
    media_files: list[MediaResponse]
