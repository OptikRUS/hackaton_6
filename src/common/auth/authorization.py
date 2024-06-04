from typing import Annotated

from fastapi import Depends
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from src.common.auth.constants import UserRoles
from src.common.auth.exceptions import AccessDeniedException
from src.common.auth.jwt_service import JWTService
from src.common.auth.schemas import UserTokenPayload


class CheckAuthorization:
    def __init__(self, permission_list: list[UserRoles] | None = None) -> None:
        self._permission_list = permission_list

    def __call__(
        self,
        jwt_manager: Annotated[JWTService, Depends(JWTService)],
        credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    ) -> UserTokenPayload:
        """
        Check access for permission list.
        """
        payload = jwt_manager.decode_token(token=credentials.credentials)
        if self._permission_list and payload.role not in self._permission_list:
            raise AccessDeniedException

        return UserTokenPayload.model_validate(payload)
