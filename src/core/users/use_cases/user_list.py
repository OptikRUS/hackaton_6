from src.core.users.models import User


class UserListUseCase:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model

    async def get_users(self, role: str) -> dict:
        users_filters = {"role": role}
        user_list = await self._user_list(filters=users_filters)
        return {"result": user_list}

    async def _user_list(self, filters: dict) -> list[User]:
        return await self.user_model.filter(**filters)
