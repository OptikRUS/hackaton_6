from src.core.trainings.models import Training


class TrainingByRoleUseCase:
    def __init__(self, training_model: Training) -> None:
        self.training_model = training_model

    async def get_trainer_trainings(self, trainer_id: int) -> dict:
        trainings = await self.training_model.filter(trainers__id=trainer_id).prefetch_related(
            "exercises__exercise__photos", "training_type"
        )
        return {"trainings": trainings}

    async def get_client_trainings(self, client_id: int) -> dict:
        trainings = await self.training_model.filter(client_id=client_id).prefetch_related(
            "exercises__exercise__photos", "training_type"
        )
        return {"trainings": trainings}
