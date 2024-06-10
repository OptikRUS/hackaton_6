from src.api.schemas.pagination import PaginationInput
from src.core.trainings.exceptions import ExerciseNotFoundError
from src.core.trainings.models import Exercise


class GetExercisesUseCase:
    def __init__(self, exercise_model: Exercise) -> None:
        self.exercise_model = exercise_model

    async def __call__(self, search: str | None, pagination: PaginationInput) -> dict:
        if search:
            exercises_qs = self.exercise_model.filter(name__icontains=search)
        else:
            exercises_qs = self.exercise_model.all()
        exercises = (
            await exercises_qs.offset(pagination.offset)
            .limit(pagination.size)
            .prefetch_related("photos")
        )
        return {"exercises": exercises}


class UpdateExercisesUseCase:
    def __init__(self, exercise_model: Exercise) -> None:
        self.exercise_model = exercise_model

    async def __call__(self, exercise_id: int, updated_data: dict) -> Exercise:
        exercise = await self.exercise_model.get_or_none(id=exercise_id)
        if not exercise:
            raise ExerciseNotFoundError
        await exercise.update_from_dict(updated_data)
        await exercise.save()
        return exercise
