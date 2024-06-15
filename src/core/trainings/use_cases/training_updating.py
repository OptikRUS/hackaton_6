import datetime

from src.core.trainings.exceptions import (
    IncorrectTrainingTimeError,
    TrainingNotFoundError,
)
from src.core.trainings.models import Training
from src.core.trainings.schemas.training import TrainingUpdating
from src.core.users.models import User


class TrainingUpdateUseCase:
    def __init__(self, training_model: Training, user_model: User) -> None:
        self.training_model = training_model
        self.user_model = user_model

    async def update_training(
        self, training_id: int, client_id: int, trainer_id: int, payload: TrainingUpdating
    ) -> Training:
        training = await self.training_model.get_or_none(id=training_id, trainer_id=trainer_id)
        if not training:
            raise TrainingNotFoundError
        await self._check_valid_training(
            start_time_of_training=payload.start_time_of_training,
            end_time_of_training=payload.end_time_of_training,
        )
        updating_data = payload.model_dump()
        updating_data["client_id"] = client_id
        updated_training = await training.update_from_dict(data=updating_data)
        await updated_training.save()
        return training

    async def _check_valid_training(
        self,
        start_time_of_training: datetime.time,
        end_time_of_training: datetime.time,
    ) -> None:
        if start_time_of_training > end_time_of_training:
            raise IncorrectTrainingTimeError
