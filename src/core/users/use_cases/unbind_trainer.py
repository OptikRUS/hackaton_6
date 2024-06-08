from src.common.auth.constants import UserRoles
from src.core.users.models import User


class UnbindTrainerUseCase:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model

    async def unbind_trainer(self, client_id: int, trainer_id: int) -> dict:
        client = await self.user_model.get_or_none(id=client_id, role=UserRoles.CLIENT.value)
        trainer = await self.user_model.get_or_none(id=trainer_id, role=UserRoles.TRAINER.value)
        await client.trainers.remove(trainer)
        return {"trainer_id": trainer.id, "client_id": client.id}
