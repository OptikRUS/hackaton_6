from src.core.trainings.models import Exercise


class GetExercisesUseCase:
    def __init__(self, exercise_model: Exercise) -> None:
        self.exercise_model = exercise_model

    async def __call__(self) -> dict:
        exercises = await self.exercise_model.all().prefetch_related("photos")
        return {"exercises": exercises}
