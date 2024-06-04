from src.core.users.exceptions import UserAlreadyExistsError
from src.core.users.models import User
from src.core.users.schemas.user import RegistrationData
from src.core.users.utils.password import generate_password_hash


class UserCreationUseCase:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model

    async def _create_user(self, data: dict) -> User:
        return await self.user_model.create(**data)

    async def register_user(self, registration_data: RegistrationData) -> User:
        user = await self.user_model.get_or_none(email=registration_data.email)
        if user:
            raise UserAlreadyExistsError
        creation_data = registration_data.model_dump(exclude={"password"})
        creation_data["password"] = generate_password_hash(registration_data.password)

        return await self._create_user(creation_data)
