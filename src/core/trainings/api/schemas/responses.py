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


class ExerciseListResponse(ApiModel):
    exercises: list[ExerciseResponse]


class TrainingUpdatingResponse(TrainingCreationResponse):
    exercises: list[ExerciseResponse]
