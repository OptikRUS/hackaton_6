from src.core.users.exceptions import UserNotFoundError
from src.core.users.models import User


class UserByIdUseCase:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model

    async def get_user_by_id(self, user_id: int) -> User:
        user = await self.user_model.get_or_none(id=user_id)
        if not user:
            raise UserNotFoundError
        return user
