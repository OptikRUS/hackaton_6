from src.api.schemas.pagination import PaginationInput
from src.core.trainings.api.schemas.requests import ExerciseListRequest
from src.core.trainings.exceptions import ExerciseNotFoundError
from src.core.trainings.models import Exercise


class GetExercisesUseCase:
    def __init__(self, exercise_model: Exercise) -> None:
        self.exercise_model = exercise_model

    async def __call__(self, search: ExerciseListRequest, pagination: PaginationInput) -> dict:
        exercises_qs = self.exercise_model.all()
        if search_filters := search.model_dump(exclude_none=True, by_alias=True):
            exercises_qs = self.exercise_model.filter(**search_filters)
        exercises: list[Exercise] = (
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
