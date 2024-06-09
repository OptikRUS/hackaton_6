from src.core.media.adapters import list_media
from src.core.media.models.media import Media
from src.core.users.schemas.media import MediaData


class GetUserMediaUseCase:
    def __init__(self, media_model: Media) -> None:
        self.file_model = media_model

    async def get_user_media(self, user_id: int) -> list[MediaData]:
        media_from_db = await self.file_model.filter(user_id=user_id)
        return list_media.validate_python(media_from_db)
