from src.core.trainings.models import Training


class TrainingByRoleUseCase:
    def __init__(self, training_model: Training) -> None:
        self.training_model = training_model

    async def get_trainer_trainings(self, trainer_id: int) -> dict:
        trainings = await self.training_model.filter(trainer_id=trainer_id).prefetch_related(
            "training_type", "exercises__training_exercise_photos", "warm_up", "warm_down"
        )
        return {"trainings": trainings}

    async def get_client_trainings(self, client_id: int) -> dict:
        trainings = await self.training_model.filter(client_id=client_id).prefetch_related(
            "training_type", "exercises__training_exercise_photos", "warm_up", "warm_down"
        )
        return {"trainings": trainings}
