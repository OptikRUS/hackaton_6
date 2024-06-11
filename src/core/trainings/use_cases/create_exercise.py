from src.core.trainings.api.schemas.requests import ExerciseCreationRequest
from src.core.trainings.models import TrainingExercise


class CreateExercisesUseCase:
    def __init__(self, training_exercise_model: TrainingExercise) -> None:
        self.training_exercise_model = training_exercise_model

    async def __call__(self, payload: ExerciseCreationRequest) -> TrainingExercise:
        return await self.training_exercise_model.create(
            **payload.model_dump(exclude_none=True, by_alias=True)
        )
