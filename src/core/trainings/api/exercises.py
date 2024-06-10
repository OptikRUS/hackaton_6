from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query, status

from src.api.schemas.pagination import PaginationInput
from src.core.trainings.api.schemas import requests, responses
from src.core.trainings.api.schemas.requests import ExerciseListRequest
from src.core.trainings.models import Exercise, TrainingExercise
from src.core.trainings.use_cases.create_exercise import CreateExercisesUseCase
from src.core.trainings.use_cases.exercises import GetExercisesUseCase, UpdateExercisesUseCase

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get("/types", response_model=responses.ExerciseListResponse, status_code=status.HTTP_200_OK)
async def get_exercises(
    pagination: Annotated[PaginationInput, Depends()],
    search: Annotated[ExerciseListRequest, Depends()],
) -> Any:
    use_case = GetExercisesUseCase(exercise_model=Exercise())
    return await use_case(search=search, pagination=pagination)


@router.put(
    "/types/{exercise_id}",
    response_model=responses.ExerciseUploadResponse,
    status_code=status.HTTP_200_OK,
)
async def update_exercises(
    exercise_id: int,
    payload: requests.ExerciseUpdateRequest,
) -> Any:
    use_case = UpdateExercisesUseCase(exercise_model=Exercise())
    return await use_case(
        exercise_id=exercise_id, updated_data=payload.model_dump(exclude_none=True)
    )


@router.post("", response_model=responses.ExerciseCreationResponse, status_code=status.HTTP_200_OK)
async def create_exercise(payload: requests.ExerciseCreationRequest) -> Any:
    use_case = CreateExercisesUseCase(training_exercise_model=TrainingExercise())
    return await use_case(payload=payload)
