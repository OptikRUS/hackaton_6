from src.api.schemas.base_schemas import ApiModel
from src.core.trainings.api.schemas.requests import TrainingCreationRequest


class TrainingCreationResponse(TrainingCreationRequest):
    ...


class TrainingTypeResponse(ApiModel):
    id: int
    title: str
    description: str | None


class TrainingTypeListResponse(ApiModel):
    training_types: list[TrainingTypeResponse]
