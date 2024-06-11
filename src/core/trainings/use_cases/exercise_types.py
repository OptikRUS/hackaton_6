from src.api.schemas.pagination import PaginationInput
from src.core.trainings.api.schemas.requests import (
    ExerciseTypeListRequest,
    TrainingExerciseUpdateRequest,
)
from src.core.trainings.exceptions import ExerciseTypeNotFoundError
from src.core.trainings.models import Exercise


class GetExerciseTypeUseCase:
    def __init__(self, exercise_type_model: Exercise) -> None:
        self.exercise_type_model = exercise_type_model

    async def __call__(self, search: ExerciseTypeListRequest, pagination: PaginationInput) -> dict:
        exercises_qs = self.exercise_type_model.all()
        if search_filters := search.model_dump(exclude_none=True, by_alias=True):
            exercises_qs = self.exercise_type_model.filter(**search_filters)
        exercises: list[Exercise] = (
            await exercises_qs.offset(pagination.offset)
            .limit(pagination.size)
            .prefetch_related("photos")
        )
        return {"exercises": exercises}


class UpdateExerciseTypeUseCase:
    def __init__(self, exercise_type_model: Exercise) -> None:
        self.exercise_type_model = exercise_type_model

    async def __call__(
        self, exercise_id: int, updated_data: dict
    ) -> Exercise:
        exercise_type = await self.exercise_type_model.get_or_none(id=exercise_id)
        if not exercise_type:
            raise ExerciseTypeNotFoundError
        await exercise_type.update_from_dict(updated_data)
        await exercise_type.save()
        return exercise_type

