from src.core.trainings.models import TrainingTemplate


class TrainingTemplatesUseCase:
    def __init__(self, training_template_model: TrainingTemplate) -> None:
        self.training_template_model = training_template_model

    async def get_training_templates(self) -> dict:
        training_templates = await self.training_template_model.all().prefetch_related(
            "exercises", "warm_up", "warm_down"
        )
        return {"templates": training_templates}
