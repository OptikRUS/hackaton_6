from src.api.schemas.pagination import PaginationInput
from src.core.trainings.models import Exercise


class GetExercisesUseCase:
    def __init__(self, exercise_model: Exercise) -> None:
        self.exercise_model = exercise_model

    async def __call__(self, pagination: PaginationInput) -> dict:
        if search_name := pagination.search:
            exercises_qs = self.exercise_model.filter(name__icontains=search_name)
        else:
            exercises_qs = self.exercise_model.all()
        exercises = (
            await exercises_qs.offset(pagination.offset)
            .limit(pagination.size)
            .prefetch_related("photos")
        )
        return {"exercises": exercises}
