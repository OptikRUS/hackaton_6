from pydantic import BaseModel, EmailStr


class LoginDataRequest(BaseModel):
    email: EmailStr
    password: str


class RegistrationDataRequest(BaseModel):
    email: EmailStr
    password: str
