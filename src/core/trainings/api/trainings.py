from typing import Any

from fastapi import APIRouter, Response, status

from src.core.trainings.api.schemas import requests as training_requests
from src.core.trainings.api.schemas import responses as training_responses
from src.core.trainings.api.schemas.responses import ExerciseListResponse
from src.core.trainings.models import Exercise, Training, TrainingType
from src.core.trainings.schemas.training import TrainingCreation, TrainingUpdating
from src.core.trainings.use_cases.exercises import GetExercisesUseCase
from src.core.trainings.use_cases.training_creation import TrainingCreationUseCase
from src.core.trainings.use_cases.training_types import TrainingTypesUseCase
from src.core.trainings.use_cases.training_updating import TrainingUpdateUseCase

router = APIRouter(prefix="/trainings", tags=["trainings"])


@router.get("", status_code=status.HTTP_200_OK)
async def get_trainings() -> Response: ...


@router.get(
    "/types",
    response_model=training_responses.TrainingTypeListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_training_types() -> Any:
    use_case = TrainingTypesUseCase(training_type_model=TrainingType())
    return await use_case.get_all_training_types()


@router.post(
    "",
    response_model=training_responses.TrainingCreationResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_training(payload: training_requests.TrainingCreationRequest) -> Any:
    use_case = TrainingCreationUseCase(
        training_model=Training(), training_type_model=TrainingType()
    )
    return await use_case.create_new_training(payload=TrainingCreation.model_validate(payload))


@router.put(
    "/{training_id}",
    response_model=training_responses.TrainingUpdatingResponse,
    status_code=status.HTTP_200_OK,
)
async def update_training(
    training_id: int, payload: training_requests.TrainingUpdatingRequest
) -> Any:
    use_case = TrainingUpdateUseCase(training_model=Training(), exercise_model=Exercise())
    return await use_case.update_training(
        training_id=training_id, payload=TrainingUpdating.model_validate(payload)
    )


@router.get("/exercises", response_model=ExerciseListResponse, status_code=status.HTTP_200_OK)
async def get_exercises() -> Any:
    use_case = GetExercisesUseCase(exercise_model=Exercise())
    return await use_case()
