from pydantic import EmailStr

from src.api.schemas.base_schemas import BaseDTO


class LoginData(BaseDTO):
    email: EmailStr
    password: str


class RegistrationData(BaseDTO):
    email: EmailStr
    password: str


class TrainerResponse(BaseDTO):
    name: str
    age: int
    rate: float


class TrainerListResponse(BaseDTO):
    result: list[TrainerResponse]
