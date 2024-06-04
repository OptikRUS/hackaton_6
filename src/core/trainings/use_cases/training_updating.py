import datetime

from src.core.trainings.exceptions import (
    IncorrectTrainingTimeError,
    TrainingNotFoundError,
)
from src.core.trainings.models import Exercise, Training
from src.core.trainings.schemas.training import TrainingUpdating


class TrainingUpdateUseCase:
    def __init__(self, training_model: Training, exercise_model: Exercise) -> None:
        self.training_model = training_model
        self.exercise_model = exercise_model

    async def update_training(self, training_id: int, payload: TrainingUpdating) -> Training:
        training = await self.training_model.get_or_none(id=training_id)
        if not training:
            raise TrainingNotFoundError
        await self._check_valid_training(
            start_time_of_training=payload.start_time_of_training,
            end_time_of_training=payload.end_time_of_training,
        )
        exercises = await self.exercise_model.filter(id__in=payload.exercises_ids)
        updating_data = payload.model_dump(exclude={"exercises_ids"})
        await training.update_from_dict(updating_data)
        await training.exercises.clear()
        await training.exercises.add(*exercises)
        await training.fetch_related("exercises")
        return training

    async def _check_valid_training(
        self,
        start_time_of_training: datetime.time,
        end_time_of_training: datetime.time,
    ) -> None:
        if start_time_of_training > end_time_of_training:
            raise IncorrectTrainingTimeError
