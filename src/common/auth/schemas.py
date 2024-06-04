import datetime

from src.api.schemas.base_schemas import ApiModel
from src.common.auth.constants import UserRoles


class UserTokenPayload(ApiModel):
    id: int
    role: UserRoles


class TokenPayload(UserTokenPayload):
    exp: datetime.datetime
    iat: datetime.datetime


class TokenData(ApiModel):
    access_token: str
