from src.core.trainings.api.schemas.requests import (
    TrainingExerciseCreationRequest,
)
from src.core.trainings.exceptions import TrainingExerciseNotFoundError
from src.core.trainings.models import ExercisePhoto, TrainingExercise


class CreateTrainingExerciseUseCase:
    def __init__(
        self, training_exercise_model: TrainingExercise, exercise_photo_model: ExercisePhoto
    ) -> None:
        self.training_exercise_model = training_exercise_model
        self.exercise_photo_model = exercise_photo_model

    async def __call__(self, payload: TrainingExerciseCreationRequest) -> TrainingExercise:
        training_exercise_data = payload.model_dump(exclude_none=True)
        training_exercise = await self.training_exercise_model.create(**training_exercise_data)
        exercise_photos = await self.exercise_photo_model.filter(
            exercise_id=training_exercise_data.pop("exercise_id")
        )
        for exercise_photo in exercise_photos:
            await exercise_photo.update_from_dict({"training_exercise_id": training_exercise.id})
            await exercise_photo.save()
        await training_exercise.fetch_related("training_exercise_photos")
        return training_exercise


class UpdateTrainingExerciseUseCase:
    def __init__(self, training_exercise_model: TrainingExercise) -> None:
        self.training_exercise_model = training_exercise_model

    async def __call__(self, training_exercise_id: int, updated_data: dict) -> TrainingExercise:
        training_exercise = await self.training_exercise_model.get_or_none(id=training_exercise_id)
        if not training_exercise:
            raise TrainingExerciseNotFoundError
        await training_exercise.update_from_dict(updated_data)
        await training_exercise.save()
        await training_exercise.fetch_related("exercise__photos")
        return training_exercise


class GetTrainingExerciseUseCase:
    def __init__(self, training_exercise_model: TrainingExercise) -> None:
        self.training_exercise_model = training_exercise_model

    async def __call__(self, training_exercise_id: int) -> TrainingExercise:
        training_exercise = await self.training_exercise_model.get_or_none(id=training_exercise_id)
        if not training_exercise:
            raise TrainingExerciseNotFoundError
        await training_exercise.fetch_related("exercise__photos")
        return training_exercise
