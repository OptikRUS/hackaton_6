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
    exercise_id: int
    distance: float | None = None
    weight: float | None = None
    height: float | None = None
    duration: float | None = None
    length: float | None = None
    count: int | None = None
    frequency: int | None = None
    description: str
