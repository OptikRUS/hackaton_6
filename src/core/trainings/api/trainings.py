from typing import Annotated, Any

from fastapi import APIRouter, Depends, status

from src.common.auth.authorization import CheckAuthorization
from src.common.auth.schemas import UserTokenPayload
from src.core.trainings.api.schemas import requests as training_requests
from src.core.trainings.api.schemas import responses as training_responses
from src.core.trainings.api.schemas.responses import TrainingListResponse
from src.core.trainings.models import Training, TrainingTemplate, TrainingType
from src.core.trainings.schemas.training import TrainingCreation, TrainingUpdating
from src.core.trainings.use_cases.get_trainings import TrainingByRoleUseCase
from src.core.trainings.use_cases.training_creation import TrainingCreationUseCase
from src.core.trainings.use_cases.training_templates import TrainingTemplatesUseCase
from src.core.trainings.use_cases.training_types import TrainingTypesUseCase
from src.core.trainings.use_cases.training_updating import TrainingUpdateUseCase
from src.core.users.models import User

router = APIRouter(prefix="/trainings", tags=["trainings"])


@router.get(
    "/trainer",
    response_model=TrainingListResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def get_trainer_trainings(
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())]
) -> Any:
    use_case = TrainingByRoleUseCase(training_model=Training())
    return await use_case.get_trainer_trainings(trainer_id=user_data.id)


@router.get(
    "/client",
    response_model=TrainingListResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def get_client_trainings(
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())]
) -> Any:
    use_case = TrainingByRoleUseCase(training_model=Training())
    return await use_case.get_client_trainings(client_id=user_data.id)


@router.get(
    "/types",
    response_model=training_responses.TrainingTypeListResponse,
    status_code=status.HTTP_200_OK,
)
async def get_training_types() -> Any:
    use_case = TrainingTypesUseCase(training_type_model=TrainingType())
    return await use_case.get_all_training_types()


@router.get(
    "/templates",
    response_model=training_responses.TrainingTemplateListResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK,
)
async def get_training_templates() -> Any:
    use_case = TrainingTemplatesUseCase(training_template_model=TrainingTemplate())
    return await use_case.get_training_templates()


@router.post(
    "",
    response_model=training_responses.TrainingCreationResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_training(
    payload: training_requests.TrainingCreationRequest,
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())],
) -> Any:
    use_case = TrainingCreationUseCase(
        training_model=Training(),
        user_model=User(),
        training_type_model=TrainingType(),
    )
    return await use_case.create_new_training(
        trainer_id=user_data.id, payload=TrainingCreation.model_validate(payload)
    )


@router.put(
    "/{training_id}",
    response_model=training_responses.TrainingUpdatingResponse,
    status_code=status.HTTP_200_OK,
)
async def update_training(
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    training_id: int,
    payload: training_requests.TrainingUpdatingRequest,
) -> Any:
    use_case = TrainingUpdateUseCase(
        training_model=Training(),
        user_model=User(),
    )
    return await use_case.update_training(
        training_id=training_id,
        client_id=payload.client_id,
        trainer_id=user_data.id,
        payload=TrainingUpdating.model_validate(payload),
    )
