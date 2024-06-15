import datetime

from pydantic import Field

from src.api.schemas.base_schemas import ApiModel
from src.core.trainings.api.schemas.requests import TrainingCreationRequest


class TrainingCreationResponse(TrainingCreationRequest):
    id: int


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
    distance: float | None
    count: int | None
    frequency: int | None
    weight: float | None
    height: float | None
    duration: float | None
    length: float | None

    photos: list[ExerciseMediaResponse] | None


class ExerciseTypeUploadResponse(ApiModel):
    id: int
    name: str | None
    muscle: str | None
    additional_muscle: str | None
    exercise_type: str | None
    equipment: str | None
    difficulty: str | None
    distance: float | None
    count: int | None
    frequency: int | None
    weight: float | None
    height: float | None
    duration: float | None
    length: float | None


class ExerciseTypeListResponse(ApiModel):
    exercises: list[ExerciseTypeResponse]


class TrainingUpdatingResponse(TrainingCreationResponse):
    id: int


class TrainingTemplateExerciseResponse(ApiModel):
    id: int
    name: str | None
    muscle: str | None
    additional_muscle: str | None
    exercise_type: str | None
    equipment: str | None
    difficulty: str | None
    distance: float | None
    count: int | None
    frequency: int | None
    weight: float | None
    height: float | None
    duration: float | None
    length: float | None


class TrainingExerciseResponse(ApiModel):
    id: int
    name: str | None
    muscle: str | None
    additional_muscle: str | None
    exercise_type: str | None
    equipment: str | None
    difficulty: str | None
    distance: float | None
    count: int | None
    frequency: int | None
    weight: float | None
    height: float | None
    duration: float | None
    length: float | None
    training_exercise_photos: list[ExerciseMediaResponse] | None = Field(alias="photos")


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


class TrainingTemplateResponse(ApiModel):
    title: str | None = ""
    description: str | None = ""
    exercises: list[TrainingTemplateExerciseResponse]


class TrainingTemplateListResponse(ApiModel):
    templates: list[TrainingTemplateResponse]
