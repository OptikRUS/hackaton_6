import datetime

from pydantic import Field

from src.api.schemas.base_schemas import ApiModel
from src.core.trainings.api.schemas.requests import TrainingCreationRequest
from src.core.trainings.constants import IntensityType


class TrainingCreationResponse(TrainingCreationRequest): ...


class TrainingTypeResponse(ApiModel):
    id: int
    title: str
    description: str | None


class TrainingTypeListResponse(ApiModel):
    training_types: list[TrainingTypeResponse]


class ExerciseMediaResponse(ApiModel):
    file_path: str


class ExerciseTypeResponse(ApiModel):
    id: int
    name: str
    muscle: str
    additional_muscle: str
    exercise_type: str
    equipment: str
    difficulty: str

    photos: list[ExerciseMediaResponse] | None


class ExerciseTypeUploadResponse(ApiModel):
    id: int
    name: str | None
    muscle: str | None
    additional_muscle: str | None
    exercise_type: str | None
    equipment: str | None
    difficulty: str | None


class ExerciseTypeListResponse(ApiModel):
    exercises: list[ExerciseTypeResponse]


class TrainingUpdatingResponse(TrainingCreationResponse):
    id: int


class TrainingExerciseResponse(ApiModel):
    id: int
    title: str
    exercise: ExerciseTypeResponse = Field(alias="exercise_type")
    distance: float | None = None
    weight_used: float | None = None
    rest_period: float | None = None
    intensity: IntensityType | None = None
    duration: float | None = None
    set_count: int | None = None
    rep_count: int | None = None
    description: str


class TrainingResponse(ApiModel):
    id: int
    title: str
    description: str | None = ""
    date_of_training: datetime.date
    start_time_of_training: datetime.time
    end_time_of_training: datetime.time
    appointed_by: str
    confirm_by_trainer: bool
    training_type: TrainingTypeResponse
    exercises: list[TrainingExerciseResponse]


class TrainingListResponse(ApiModel):
    trainings: list[TrainingResponse]
