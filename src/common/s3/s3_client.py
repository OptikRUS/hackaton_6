from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import aioboto3
from botocore.client import BaseClient

from src.config.settings import settings


async def get_s3_client() -> AsyncGenerator[BaseClient, None]:
    session = aioboto3.Session()
    async with session.client(
        "s3",
        endpoint_url=settings.S3.get_s3_url,
        aws_access_key_id=settings.S3.ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3.SECRET_ACCESS_KEY,
        use_ssl=settings.S3.USE_SSL,
    ) as client:
        yield client


s3_context = asynccontextmanager(get_s3_client)
