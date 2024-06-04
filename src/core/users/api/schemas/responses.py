from pydantic import BaseModel, EmailStr

from src.common.auth.constants import UserRoles
from src.core.users.constants import GenderType


class UserResponse(BaseModel):
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
