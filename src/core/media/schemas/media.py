from src.api.schemas.base_schemas import BaseDTO


class MediaData(BaseDTO):
    id: int
    user_id: int
    file_path: str
