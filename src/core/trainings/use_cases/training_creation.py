import datetime

from src.core.trainings.exceptions import (
    IncorrectTrainingTimeError,
    TrainingAlreadyExistsError,
    TrainingTypeNotFoundError,
)
from src.core.trainings.models import Exercise, Training, TrainingType
from src.core.trainings.schemas.training import TrainingCreation
from src.core.users.models import User


class TrainingCreationUseCase:
    def __init__(
        self, training_model: Training, training_type_model: TrainingType, user_model: User
    ) -> None:
        self.training_model = training_model
        self.training_type_model = training_type_model
        self.user_model = user_model

    async def create_new_training(self, trainer_id: int, payload: TrainingCreation) -> Training:
        await self._check_valid_type_of_training(training_type_id=payload.training_type_id)
        await self._check_valid_training(
            date_of_training=payload.date_of_training,
            start_time_of_training=payload.start_time_of_training,
            end_time_of_training=payload.end_time_of_training,
        )
        training_data = payload.model_dump()
        training_data["trainer_id"] = trainer_id
        new_training = await self._create_training(data=training_data)
        warm_up_exercises = await Exercise.filter(name__icontains="вело").limit(3)
        warm_down_exercises = await Exercise.filter(name__icontains="растяжка").limit(3)
        await new_training.warm_up.add(*warm_up_exercises)
        await new_training.warm_down.add(*warm_down_exercises)
        await new_training.save()
        await new_training.fetch_related("warm_up", "warm_down")
        return new_training

    async def _create_training(self, data: dict) -> Training:
        return await self.training_model.create(**data)

    async def _check_valid_type_of_training(self, training_type_id: int) -> None:
        training_type = await self.training_type_model.get_or_none(id=training_type_id)
        if not training_type:
            raise TrainingTypeNotFoundError

    async def _check_valid_training(
        self,
        date_of_training: datetime.date,
        start_time_of_training: datetime.time,
        end_time_of_training: datetime.time,
    ) -> None:
        if start_time_of_training > end_time_of_training:
            raise IncorrectTrainingTimeError
        training_is_exist = await self.training_model.get_or_none(
            date_of_training=date_of_training, start_time_of_training=start_time_of_training
        )
        if training_is_exist:
            raise TrainingAlreadyExistsError
