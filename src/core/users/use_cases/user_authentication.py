from src.common.auth.jwt_service import JWTService
from src.common.auth.schemas import TokenData, UserTokenPayload
from src.core.users.exceptions import IncorrectCredentials
from src.core.users.models import User
from src.core.users.schemas.user import LoginData
from src.core.users.utils.password import verify_password_hash


class UserAuthenticationUseCase:
    def __init__(self, user_model: User, jwt_service: JWTService) -> None:
        self._jwt_service = jwt_service
        self._user_model = user_model

    async def auth_user(self, login_data: LoginData) -> TokenData:
        user = await self._user_model.get_or_none(email=login_data.email)

        if not user:
            raise IncorrectCredentials
        if not verify_password_hash(password=login_data.password, hashed_password=user.password):
            raise IncorrectCredentials

        return self._jwt_service.encode_token(payload=UserTokenPayload(id=user.id, role=user.role))
