from typing import Annotated, Any

from fastapi import APIRouter, Depends, status

from src.common.auth.authorization import CheckAuthorization
from src.common.auth.constants import UserRoles
from src.common.auth.jwt_service import JWTService
from src.common.auth.schemas import TokenData, UserTokenPayload
from src.core.users.api.schemas.requests import LoginDataRequest, RegistrationDataRequest
from src.core.users.api.schemas.responses import (
    TrainerListResponse,
    UnBindTrainerRequest,
    UnBindTrainerResponse,
    UserResponse,
)
from src.core.users.models import User
from src.core.users.schemas.user import LoginData, RegistrationData
from src.core.users.use_cases.bind_trainer import BindTrainerUseCase
from src.core.users.use_cases.unbind_trainer import UnbindTrainerUseCase
from src.core.users.use_cases.user_authentication import UserAuthenticationUseCase
from src.core.users.use_cases.user_by_id import UserByIdUseCase
from src.core.users.use_cases.user_creation import UserCreationUseCase
from src.core.users.use_cases.user_list import UserListUseCase

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/auth", response_model=TokenData, status_code=status.HTTP_201_CREATED)
async def auth_user(login_data: LoginDataRequest) -> Any:
    use_case = UserAuthenticationUseCase(user_model=User(), jwt_service=JWTService())
    return await use_case.auth_user(login_data=LoginData.model_validate(login_data))


@router.post("/registration", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def registrate_user(registration_data: RegistrationDataRequest) -> Any:
    use_case = UserCreationUseCase(user_model=User())
    return await use_case.register_user(
        registration_data=RegistrationData.model_validate(registration_data)
    )


@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_me(user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())]) -> Any:
    use_case = UserByIdUseCase(user_model=User())
    return await use_case.get_user_by_id(user_id=user_data.id)


@router.get("/trainers", response_model=TrainerListResponse, status_code=status.HTTP_200_OK)
async def get_trainers() -> Any:
    use_case = UserListUseCase(user_model=User())
    role = UserRoles.TRAINER.value
    return await use_case.get_users(role=role)


@router.get("/clients", response_model=TrainerListResponse, status_code=status.HTTP_200_OK)
async def get_clients() -> Any:
    use_case = UserListUseCase(user_model=User())
    role = UserRoles.CLIENT.value
    return await use_case.get_users(role=role)


@router.post(
    "/trainers/bind",
    status_code=status.HTTP_200_OK,
    response_model=UnBindTrainerResponse,
)
async def bind_trainer(
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    payload: UnBindTrainerRequest,
) -> Any:
    use_case = BindTrainerUseCase(user_model=User())
    return await use_case.bind_trainer(client_id=user_data.id, trainer_id=payload.trainer_id)


@router.delete(
    "/trainers/unbind",
    status_code=status.HTTP_200_OK,
    response_model=UnBindTrainerResponse,
)
async def unbind_trainer(
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    payload: UnBindTrainerRequest,
) -> Any:
    use_case = UnbindTrainerUseCase(user_model=User())
    return await use_case.unbind_trainer(client_id=user_data.id, trainer_id=payload.trainer_id)