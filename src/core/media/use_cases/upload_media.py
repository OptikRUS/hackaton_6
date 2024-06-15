from botocore.client import BaseClient

from src.config.settings import settings
from src.core.media.exceptions import UnsupportedFileTypeError
from src.core.media.models.media import Media
from src.core.media.utils import generate_valid_file_path
from src.core.media.validators import validate_file_type


class UploadMediaUseCase:
    def __init__(self, s3_client: BaseClient, media_model: Media) -> None:
        self.media_model = media_model
        self.s3_client = s3_client

    async def upload_media(
        self,
        content: bytes,
        file_name: str,
        user_id: int,
        content_type: str,
        folder_path: str | int = None
    ) -> str:
        if not validate_file_type(content_type=content_type, file_name=file_name):
            raise UnsupportedFileTypeError

        if folder_path:
            folder_path = f"{folder_path}/{user_id}"
        else:
            folder_path = user_id

        file_path = generate_valid_file_path(
            content_type=content_type,
            file_name=file_name,
            folder_path=folder_path,
        )
        async with self.s3_client as s3:
            await s3.put_object(
                Bucket=settings.S3.BUCKET_NAME,
                Key=file_path,
                Body=content,
                ContentType=content_type,
            )
        await self.media_model.create(user_id=user_id, file_path=file_path)

        return file_path
