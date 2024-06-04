from src.common.auth.constants import UserRoles
from src.core.users.models import User


class UserListUseCase:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model

    async def get_trainers(self) -> dict:
        trainers_filters = {"role": UserRoles.TRAINER.value}
        all_trainers = await self._user_list(filters=trainers_filters)
        return {"result": all_trainers}

    async def _user_list(self, filters: dict) -> list[User]:
        return await self.user_model.filter(**filters)
