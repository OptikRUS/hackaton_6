import datetime

from src.api.schemas.base_schemas import ApiModel


class TrainingCreationRequest(ApiModel):
    title: str
    training_type_id: int
    description: str | None = ""
    date_of_training: datetime.date
    start_time_of_training: datetime.time
    end_time_of_training: datetime.time
