from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query, status

from src.api.schemas.pagination import PaginationInput
from src.core.trainings.api.schemas.requests import ExerciseCreationRequest
from src.core.trainings.api.schemas.responses import ExerciseCreationResponse, ExerciseListResponse
from src.core.trainings.models import Exercise, TrainingExercise
from src.core.trainings.use_cases.create_exercise import CreateExercisesUseCase
from src.core.trainings.use_cases.exercises import GetExercisesUseCase

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get("/types", response_model=ExerciseListResponse, status_code=status.HTTP_200_OK)
async def get_exercises(
    pagination: Annotated[PaginationInput, Depends()],
    search: Annotated[str | None, Query(max_length=50)] = None,
) -> Any:
    use_case = GetExercisesUseCase(exercise_model=Exercise())
    return await use_case(search=search, pagination=pagination)


@router.post("", response_model=ExerciseCreationResponse, status_code=status.HTTP_200_OK)
async def create_exercise(payload: ExerciseCreationRequest) -> Any:
    use_case = CreateExercisesUseCase(training_exercise_model=TrainingExercise())
    return await use_case(payload=payload)
