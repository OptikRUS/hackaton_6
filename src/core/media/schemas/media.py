from typing import Any

from src.api.schemas.base_schemas import BaseDTO


class StreamingMedia(BaseDTO):
    stream_reader: Any
    content_len: str
    content_type: str
