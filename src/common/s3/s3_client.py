import aioboto3
from botocore.client import BaseClient

from src.config.settings import settings

s3_session = aioboto3.Session()


def get_s3_client() -> BaseClient:
    client = s3_session.client(
        "s3",
        endpoint_url=settings.S3.get_s3_url,
        aws_access_key_id=settings.S3.ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3.SECRET_ACCESS_KEY,
        use_ssl=settings.S3.USE_SSL
    )

    return client
