from botocore.client import BaseClient
from botocore.errorfactory import ClientError

from src.config.settings import settings
from src.core.media.exceptions import MediaNotFoundError


class GetMediaUseCase:
    def __init__(self, s3_client: BaseClient) -> None:
        self.s3_client = s3_client

    async def get_media_by_path(self, file_path: str) -> bytes:
        async with self.s3_client as s3:
            try:
                response = await s3.get_object(Bucket=settings.S3.BUCKET_NAME, Key=file_path)
            except ClientError:
                raise MediaNotFoundError
            file_bytes = await response.get('Body').read()

        return file_bytes
