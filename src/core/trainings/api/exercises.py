from typing import Annotated, Any

from fastapi import APIRouter, Depends, status

from src.api.schemas.pagination import PaginationInput
from src.core.trainings.api.schemas import requests, responses
from src.core.trainings.api.schemas.requests import ExerciseTypeListRequest
from src.core.trainings.models import Exercise, ExercisePhoto, TrainingExercise
from src.core.trainings.use_cases.exercise_types import (
    GetExerciseTypeUseCase,
    UpdateExerciseTypeUseCase,
)
from src.core.trainings.use_cases.training_exercise import (
    CreateTrainingExerciseUseCase,
    GetTrainingExerciseUseCase,
    UpdateTrainingExerciseUseCase,
)

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get(
    "/types",
    response_model=responses.ExerciseTypeListResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def get_exercise_types(
    pagination: Annotated[PaginationInput, Depends()],
    search: Annotated[ExerciseTypeListRequest, Depends()],
) -> Any:
    use_case = GetExerciseTypeUseCase(exercise_type_model=Exercise())
    return await use_case(search=search, pagination=pagination)


@router.put(
    "/types/{exercise_id}",
    response_model=responses.ExerciseTypeUploadResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def update_exercise_type(
    exercise_id: int,
    payload: requests.ExerciseTypeUpdateRequest,
) -> Any:
    use_case = UpdateExerciseTypeUseCase(exercise_type_model=Exercise())
    return await use_case(
        exercise_id=exercise_id, updated_data=payload.model_dump(exclude_none=True)
    )


@router.post(
    "",
    response_model=responses.TrainingExerciseResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def create_training_exercise(payload: requests.TrainingExerciseCreationRequest) -> Any:
    use_case = CreateTrainingExerciseUseCase(
        training_exercise_model=TrainingExercise(), exercise_photo_model=ExercisePhoto()
    )
    return await use_case(payload=payload)


@router.put(
    "/{exercise_id}",
    response_model=responses.TrainingExerciseResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def update_training_exercise(
    exercise_id: int, payload: requests.TrainingExerciseUpdateRequest
) -> Any:
    use_case = UpdateTrainingExerciseUseCase(training_exercise_model=TrainingExercise())
    return await use_case(
        training_exercise_id=exercise_id, updated_data=payload.model_dump(exclude_none=True)
    )


@router.get(
    "/{exercise_id}",
    response_model=responses.TrainingExerciseResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def get_training_exercise(exercise_id: int) -> Any:
    use_case = GetTrainingExerciseUseCase(training_exercise_model=TrainingExercise())
    return await use_case(training_exercise_id=exercise_id)
