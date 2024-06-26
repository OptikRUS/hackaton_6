from random import choice

from faker import Faker

from src.core.trainings.models import Exercise, TrainingTemplate

make_mock = Faker("ru_RU")


async def fill_training_templates(count: int = 50) -> None:
    await TrainingTemplate.all().delete()
    exercises = await Exercise.all()
    training_templates = [
        {
            "title": f"Шаблон тренировки № {i}",
            "description": f"Описание для тренировки № {i}",
        }
        for i in range(1, count)
    ]
    warm_up_exercises = await Exercise.filter(name__icontains="вело").limit(3)
    warm_down_exercises = await Exercise.filter(name__icontains="растяжка").limit(3)
    for training_type in training_templates:
        exercises_for_training_template = [choice(exercises) for _ in range(3)]
        training_template, is_created = await TrainingTemplate.update_or_create(**training_type)
        await training_template.exercises.add(*exercises_for_training_template)
        await training_template.warm_up.add(*warm_up_exercises)
        await training_template.warm_down.add(*warm_down_exercises)
        await training_template.exercises.add(*exercises_for_training_template)
        await training_template.save()
