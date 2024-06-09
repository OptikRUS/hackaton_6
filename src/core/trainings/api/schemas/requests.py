import datetime

from src.api.schemas.base_schemas import ApiModel


class TrainingCreationRequest(ApiModel):
    title: str
    training_type_id: int
    description: str | None = ""
    date_of_training: datetime.date
    start_time_of_training: datetime.time
    end_time_of_training: datetime.time


class TrainingUpdatingRequest(TrainingCreationRequest):
    client_id: int


class ExerciseCreationRequest(ApiModel):
    title: str
    training_id: int
    exercise_id: int
    distance: float | None = None
    weight: float | None = None
    height: float | None = None
    duration: float | None = None
    length: float | None = None
    count: int | None = None
    frequency: int | None = None
    description: str = ""
