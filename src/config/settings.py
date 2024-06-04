from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    NAME: str = "hackaton_template"
    VERSION: str = "0.1.0"
    ADDRESS: str = "0.0.0.0"  # noqa: S104
    PORT: int = 8080
    OPENAPI_PREFIX: str = ""

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env", extra="ignore")


class DatabaseSettings(BaseSettings):
    PROTOCOL: str = "postgres"
    HOST: str = "localhost"
    PORT: str = "5432"
    USER: str = "postgres"
    PASSWORD: SecretStr = SecretStr("postgres")
    NAME: str = "postgres"

    model_config = SettingsConfigDict(env_prefix="DB_", env_file=".env", extra="ignore")

    @property
    def URL(self) -> SecretStr:  # noqa: N802
        return SecretStr(
            f"{self.PROTOCOL}://{self.USER}:{self.PASSWORD.get_secret_value()}@{self.HOST}:{self.PORT}/{self.NAME}",
        )


class CORSSettings(BaseSettings):
    CREDENTIALS: bool = True
    METHODS: list[str] = ["*"]
    HEADERS: list[str] = ["*", "Authorization"]
    ORIGINS: list[str] = []

    model_config = SettingsConfigDict(env_prefix="CORS_", env_file=".env", extra="ignore")


class JWTSettings(BaseSettings):
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = "secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_prefix="JWT_", env_file=".env", extra="ignore")


class S3Settings(BaseSettings):
    MINIO_PORT: int = 9001
    MINIO_HOST: str = "0.0.0.0"
    BUCKET_NAME: str = "your-bucket-name"
    ACCESS_KEY_ID: str = "minioadmin"
    SECRET_ACCESS_KEY: str = "minioadmin"
    USE_SSL: bool = False

    model_config = SettingsConfigDict(env_prefix="S3_", env_file=".env", extra="ignore")

    @property
    def get_s3_url(self) -> str:
        http_prefix = "https" if self.USE_SSL else "http"
        return f"{http_prefix}://{self.MINIO_HOST}:{self.MINIO_PORT}"


class Settings(BaseSettings):
    APP: AppSettings = AppSettings()
    DATABASE: DatabaseSettings = DatabaseSettings()
    CORS: CORSSettings = CORSSettings()
    JWT: JWTSettings = JWTSettings()
    S3: S3Settings = S3Settings()


settings = Settings()
