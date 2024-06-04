import datetime

from jose import JWTError, jwt

from src.common.auth.exceptions import InvalidTokenException
from src.common.auth.schemas import TokenData, TokenPayload, UserTokenPayload
from src.config.settings import settings


class JWTService:
    def encode_token(self, payload: UserTokenPayload) -> TokenData:
        copy_payload: dict = payload.model_dump()

        iat = datetime.datetime.now(datetime.UTC)
        access_exp = iat + datetime.timedelta(minutes=settings.JWT.ACCESS_TOKEN_EXPIRE_MINUTES)

        access_jwt = self._generate_token(payload=copy_payload, iat=iat, exp=access_exp)

        return TokenData(access_token=access_jwt)

    @staticmethod
    def _generate_token(payload: dict, iat: datetime.datetime, exp: datetime.datetime) -> str:
        payload.update({"iat": iat, "exp": exp})

        return jwt.encode(payload, settings.JWT.SECRET_KEY, algorithm=settings.JWT.ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> TokenPayload:
        try:
            payload = jwt.decode(
                token,
                settings.JWT.SECRET_KEY,
                algorithms=[settings.JWT.ALGORITHM],
            )
        except JWTError as err:
            raise InvalidTokenException from err

        return TokenPayload.model_validate(payload)
