from typing import Any

from fastapi import APIRouter, Response, status

from src.core.trainings.api.schemas import requests as training_requests
from src.core.trainings.api.schemas import responses as training_responses
from src.core.trainings.models import Training, TrainingType
from src.core.trainings.schemas.training import TrainingCreation
from src.core.trainings.use_cases.training_creation import TrainingCreationUseCase
from src.core.trainings.use_cases.training_types import TrainingTypesUseCase

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
