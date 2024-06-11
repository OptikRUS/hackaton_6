import typing

from botocore.client import BaseClient
from fastapi import APIRouter, Depends, File, UploadFile, status

from src.common.auth.authorization import CheckAuthorization
from src.common.auth.constants import UserRoles
from src.common.auth.jwt_service import JWTService
from src.common.auth.schemas import TokenData, UserTokenPayload
from src.common.s3.s3_client import get_s3_client
from src.core.media.models import Media
from src.core.users.api.schemas import responses
from src.core.users.api.schemas.requests import LoginDataRequest, RegistrationDataRequest
from src.core.users.models import User
from src.core.users.schemas.user import LoginData, RegistrationData
from src.core.users.use_cases.bind_trainer import BindTrainerUseCase
from src.core.users.use_cases.get_user_media import GetUserMediaUseCase
from src.core.users.use_cases.set_user_avatar import SetUserAvatarUseCase
from src.core.users.use_cases.unbind_trainer import UnbindTrainerUseCase
from src.core.users.use_cases.user_authentication import UserAuthenticationUseCase
from src.core.users.use_cases.user_by_id import UserByIdUseCase
from src.core.users.use_cases.user_creation import UserCreationUseCase
from src.core.users.use_cases.user_list import UserListUseCase

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/auth", response_model=TokenData, status_code=status.HTTP_201_CREATED)
async def auth_user(login_data: LoginDataRequest) -> typing.Any:
    use_case = UserAuthenticationUseCase(user_model=User(), jwt_service=JWTService())
    return await use_case.auth_user(login_data=LoginData.model_validate(login_data))


@router.post("/registration", response_model=responses.UserResponse, status_code=status.HTTP_200_OK)
async def registrate_user(registration_data: RegistrationDataRequest) -> typing.Any:
    use_case = UserCreationUseCase(user_model=User())
    return await use_case.register_user(
        registration_data=RegistrationData.model_validate(registration_data)
    )


@router.get("/me", response_model=responses.UserResponse, status_code=status.HTTP_200_OK)
async def get_me(
    user_data: typing.Annotated[UserTokenPayload, Depends(CheckAuthorization())]
) -> typing.Any:
    use_case = UserByIdUseCase(user_model=User())
    return await use_case.get_user_by_id(user_id=user_data.id)


@router.get("/trainers", response_model=responses.TrainerListResponse, status_code=status.HTTP_200_OK)
async def get_trainers() -> typing.Any:
    use_case = UserListUseCase(user_model=User())
    role = UserRoles.TRAINER.value
    return await use_case.get_users(role=role)


@router.get("/clients", response_model=responses.ClientListResponse, status_code=status.HTTP_200_OK)
async def get_clients() -> typing.Any:
    use_case = UserListUseCase(user_model=User())
    role = UserRoles.CLIENT.value
    return await use_case.get_users(role=role)


@router.post(
    "/trainers/bind",
    status_code=status.HTTP_200_OK,
    response_model=responses.UnBindTrainerResponse,
)
async def bind_trainer(
    user_data: typing.Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    payload: responses.UnBindTrainerRequest,
) -> typing.Any:
    use_case = BindTrainerUseCase(user_model=User())
    return await use_case.bind_trainer(client_id=user_data.id, trainer_id=payload.trainer_id)


@router.delete(
    "/trainers/unbind",
    status_code=status.HTTP_200_OK,
    response_model=responses.UnBindTrainerResponse,
)
async def unbind_trainer(
    user_data: typing.Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    payload: responses.UnBindTrainerRequest,
) -> typing.Any:
    use_case = UnbindTrainerUseCase(user_model=User())
    return await use_case.unbind_trainer(client_id=user_data.id, trainer_id=payload.trainer_id)


@router.get("/user_media", response_model=responses.UserMediaResponse, status_code=status.HTTP_200_OK)
async def get_user_media(
    user_data: typing.Annotated[UserTokenPayload, Depends(CheckAuthorization())],
):
    use_case = GetUserMediaUseCase(media_model=Media())
    result = await use_case.get_user_media(user_id=user_data.id)
    return responses.UserMediaResponse(media_files=result)


@router.put("/set_avatar", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def set_user_avatar(
    s3_client: typing.Annotated[BaseClient, Depends(get_s3_client)],
    user_data: typing.Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    file: UploadFile = File(...),
):
    use_case = SetUserAvatarUseCase(user_model=User(), media_model=Media(), s3_client=s3_client)
    file_content = await file.read()
    await use_case.set_user_avatar(
        content=file_content,
        file_name=file.filename,
        user_id=user_data.id,
        content_type=file.content_type,
    )
