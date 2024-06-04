import json

from src.config.settings import settings
from src.core.trainings.models import Exercise


async def fill_exercises() -> None:
    with open(f"{settings.DIRS.ROOT}/dataset/main_images.json", encoding="utf-8") as file:
        file_data = json.load(file)
        for row in file_data:
            await Exercise.update_or_create(
                name=row["name"],
                muscle=row["muscle"],
                additional_muscle=row["additionalMuscle"],
                exercise_type=row["type"],
                equipment=row["equipment"],
                difficulty=row["difficulty"],
            )
