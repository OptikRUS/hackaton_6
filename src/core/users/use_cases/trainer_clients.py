from src.core.users.models import User


class TrainerClientsListUseCase:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model

    async def get_clients(self, trainer_id: int) -> dict:
        trainer = await self.user_model.get_or_none(id=trainer_id).prefetch_related("clients")
        return {"result": trainer.clients}
