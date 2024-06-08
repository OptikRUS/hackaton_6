from typing import TYPE_CHECKING, Annotated

from botocore.client import BaseClient
from fastapi import APIRouter, Depends, File, UploadFile, status
from starlette.responses import StreamingResponse

from src.common.auth.authorization import CheckAuthorization
from src.common.auth.schemas import UserTokenPayload
from src.common.s3.s3_client import get_s3_client
from src.core.media.models import Media
from src.core.media.schemas.media import MediaData
from src.core.media.use_cases.get_media import GetMediaUseCase
from src.core.media.use_cases.get_user_media import GetUserMediaUseCase
from src.core.media.use_cases.upload_media import UploadMediaUseCase

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

router = APIRouter(prefix="/media", tags=["media"])


@router.post(
    "/upload",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def upload_file(
    s3_client: Annotated[BaseClient, Depends(get_s3_client)],
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())],
    file: UploadFile = File(...),
):
    use_case = UploadMediaUseCase(s3_client=s3_client, media_model=Media())
    file_content = await file.read()
    await use_case.upload_media(
        content=file_content,
        file_name=file.filename,
        user_id=user_data.id,
        content_type=file.content_type
    )


@router.get(
    "/user_media",
    response_model=list[MediaData],
    status_code=status.HTTP_200_OK
)
async def get_user_media(
    user_data: Annotated[UserTokenPayload, Depends(CheckAuthorization())],
):
    use_case = GetUserMediaUseCase(media_model=Media())
    return await use_case.get_user_media(user_id=user_data.id)


@router.get(
    "/{file_path:path}",
    response_model=bytes,
    status_code=status.HTTP_200_OK
)
async def get_media_by_path(
    file_path: str,
    s3_client: Annotated[BaseClient, Depends(get_s3_client)],
):
    use_case = GetMediaUseCase(s3_client=s3_client)
    file_info: tuple[AsyncGenerator, str] = await use_case.get_media_by_path(
        file_path=file_path
    )
    return StreamingResponse(
        file_info[0],
        media_type="application/octet-stream",
        headers={"content-length": file_info[1]}
    )
