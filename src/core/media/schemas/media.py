from typing import Any

from pydantic import ConfigDict

from src.api.schemas.base_schemas import BaseDTO


class MediaData(BaseDTO):
    id: int
    user_id: int
    file_path: str


class StreamingMedia(BaseDTO):
    stream_reader: Any
    content_len: str
    content_type: str
