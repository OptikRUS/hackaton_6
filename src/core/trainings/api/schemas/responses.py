import datetime

from pydantic import Field

from src.api.schemas.base_schemas import ApiModel
from src.core.trainings.api.schemas.requests import TrainingCreationRequest


class TrainingCreationResponse(TrainingCreationRequest): ...


class TrainingTypeResponse(ApiModel):
    id: int
    title: str
    description: str | None


class TrainingTypeListResponse(ApiModel):
    training_types: list[TrainingTypeResponse]


class ExerciseMediaResponse(ApiModel):
    file_path: str


class ExerciseResponse(ApiModel):
    id: int
    name: str
    muscle: str
    additional_muscle: str
    exercise_type: str
    equipment: str
    difficulty: str

    photos: list[ExerciseMediaResponse]


class ExerciseUploadResponse(ApiModel):
    id: int
    name: str | None
    muscle: str | None
    additional_muscle: str | None
    exercise_type: str | None
    equipment: str | None
    difficulty: str | None


class ExerciseListResponse(ApiModel):
    exercises: list[ExerciseResponse]


class TrainingUpdatingResponse(TrainingCreationResponse):
    id: int


class ExerciseCreationResponse(ApiModel):
    title: str
    training_id: int
    exercise_id: int = Field(alias="exercise_type_id")
    distance: float | None = None
    weight: float | None = None
    height: float | None = None
    duration: float | None = None
    length: float | None = None
    count: int | None = None
    frequency: int | None = None
    description: str


class TrainingExerciseResponse(ApiModel):
    id: int
    title: str
    exercise: ExerciseResponse = Field(alias="exercise_type")
    distance: float | None = None
    weight: float | None = None
    height: float | None = None
    duration: float | None = None
    length: float | None = None
    count: int | None = None
    frequency: int | None = None
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
