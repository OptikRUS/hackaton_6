from pydantic import TypeAdapter

from src.core.users.schemas.media import MediaData

list_media = TypeAdapter(list[MediaData])
