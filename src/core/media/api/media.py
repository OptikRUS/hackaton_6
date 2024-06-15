from typing import Annotated

from botocore.client import BaseClient
from fastapi import APIRouter, Depends, File, UploadFile, status, Body
from starlette.responses import StreamingResponse

from src.common.auth.authorization import CheckAuthorization
from src.common.auth.schemas import UserTokenPayload
from src.common.s3.s3_client import get_s3_client
from src.core.media.models import Media
from src.core.media.schemas.media import StreamingMedia
from src.core.media.use_cases.get_media import GetMediaUseCase
from src.core.media.use_cases.upload_media import UploadMediaUseCase

router = APIRouter(prefix="/media", tags=["media"])


@router.post("/upload", response_model=str, status_code=status.HTTP_200_OK)
async def upload_file(
    s3_client: Annotated[BaseClient, Depends(get_s3_client)],
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    file: UploadFile = File(...),
    folder_path: str = Body(default=None)
):
    use_case = UploadMediaUseCase(s3_client=s3_client, media_model=Media())
    file_content = await file.read()
    return await use_case.upload_media(
        content=file_content,
        file_name=file.filename,
        user_id=user_data.id,
        content_type=file.content_type,
        folder_path=folder_path
    )


@router.get("/{file_path:path}", response_model=bytes, status_code=status.HTTP_200_OK)
async def get_media_by_path(
    file_path: str,
    s3_client: Annotated[BaseClient, Depends(get_s3_client)],
):
    use_case = GetMediaUseCase(s3_client=s3_client)
    file_info: StreamingMedia = await use_case.get_media_by_path(file_path=file_path)
    return StreamingResponse(
        file_info.stream_reader,
        media_type=file_info.content_type,
        headers={"content-length": file_info.content_len},
    )
