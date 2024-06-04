from pydantic import TypeAdapter

from src.core.media.schemas.media import MediaData

list_media = TypeAdapter(list[MediaData])
