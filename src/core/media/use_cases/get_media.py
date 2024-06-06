import asyncio
from typing import AsyncGenerator

from botocore.client import BaseClient
from botocore.errorfactory import ClientError

from src.config.settings import settings
from src.core.media.exceptions import MediaNotFoundError


class GetMediaUseCase:
    def __init__(self, s3_client: BaseClient) -> None:
        self.s3_client = s3_client

    async def get_media_by_path(self, file_path: str) -> tuple[AsyncGenerator, str]:
        async with self.s3_client as s3:
            try:
                response = await s3.get_object(Bucket=settings.S3.BUCKET_NAME, Key=file_path)
            except ClientError:
                raise MediaNotFoundError
            file_stream = response.get('Body')
            content_len = response.get("ContentLength")
            stream_reader = asyncio.StreamReader()
            async for chunk in file_stream:
                stream_reader.feed_data(chunk)

        async def _file_streamer() -> AsyncGenerator:
            while not stream_reader.at_eof():
                yield await stream_reader.read(2048)

        return _file_streamer(), str(content_len)
