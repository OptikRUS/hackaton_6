from typing import AsyncGenerator

from botocore.client import BaseClient
from botocore.errorfactory import ClientError
from botocore.response import StreamingBody
from src.config.settings import settings
from src.core.media.exceptions import MediaNotFoundError
from src.core.media.schemas.media import StreamingMedia
from src.core.media.utils import streaming_file


class GetMediaUseCase:
    def __init__(self, s3_client: BaseClient) -> None:
        self.s3_client = s3_client

    async def get_media_by_path(self, file_path: str) -> StreamingMedia:
        async with self.s3_client as s3:
            try:
                response = await s3.get_object(Bucket=settings.S3.BUCKET_NAME, Key=file_path)
            except ClientError:
                raise MediaNotFoundError
            file_stream: StreamingBody = response.get('Body')
            read_file = await file_stream.read()

        return StreamingMedia(
            stream_reader=streaming_file(data=read_file, chunk_size=2048),
            content_len=str(file_stream.content_length),  # type: ignore
            content_type=file_stream.content_type  # type: ignore
        )
