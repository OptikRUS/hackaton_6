from src.core.trainings.models import TrainingType


class TrainingTypesUseCase:
    def __init__(self, training_type_model: TrainingType) -> None:
        self.training_type_model = training_type_model

    async def get_all_training_types(self) -> dict:
        all_training_types = await self.training_type_model.all()
        return {"training_types": all_training_types}
