import asyncio
import json
import mimetypes

import aiofiles

from src.common.s3.s3_client import get_s3_client
from src.config.settings import settings
from src.core.trainings.models import Exercise, ExercisePhoto


async def fill_exercises() -> None:
    file_paths = list()
    with open(f"{settings.DIRS.ROOT}/dataset/main_images.json", encoding="utf-8") as file:
        file_data = json.load(file)
        for row in file_data:
            exercise = await Exercise.update_or_create(
                name=row["name"],
                muscle=row["muscle"],
                additional_muscle=row["additionalMuscle"],
                exercise_type=row["type"],
                equipment=row["equipment"],
                difficulty=row["difficulty"],
            )
            for photo_path in row["photos"]:
                file_paths.append(photo_path)
                exercise_photo_path = f"exercise/{photo_path}"
                await ExercisePhoto.update_or_create(
                    exercise_id=exercise[0].id, file_path=exercise_photo_path
                )

    async def upload_file(file_path: str) -> None:
        async with aiofiles.open(f"{settings.DIRS.ROOT}/dataset/{file_path}", "rb") as file_data:
            data = await file_data.read()
            mime_type, _ = mimetypes.guess_type(file_path)
            async with get_s3_client() as s3:
                await s3.put_object(
                    Bucket=settings.S3.BUCKET_NAME,
                    Key=f"exercise/{file_path}",
                    Body=data,
                    ContentType=mime_type,
                )

    for i in range(0, len(file_paths), 15):
        tasks = [upload_file(file) for file in file_paths[i : i + 15]]
        await asyncio.gather(*tasks)
