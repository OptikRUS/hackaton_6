from typing import Annotated, Any

from fastapi import APIRouter, Depends, status

from src.common.auth.authorization import CheckAuthorization
from src.common.auth.jwt_service import JWTService
from src.common.auth.schemas import TokenData, UserTokenPayload
from src.core.users.api.schemas.requests import LoginDataRequest, RegistrationDataRequest
from src.core.users.api.schemas.responses import UserResponse
from src.core.users.models import User
from src.core.users.schemas.user import LoginData, RegistrationData, TrainerListResponse
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
async def get_me(
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())]
) -> Any:
    use_case = UserByIdUseCase(user_model=User())
    return await use_case.get_user_by_id(user_id=user_data.id)


@router.get("/trainers", response_model=TrainerListResponse, status_code=status.HTTP_200_OK)
async def get_trainers() -> Any:
    use_case = UserListUseCase(user_model=User())
    return await use_case.get_trainers()


