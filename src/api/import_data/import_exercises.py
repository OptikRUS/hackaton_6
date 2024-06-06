from fastapi import APIRouter, Response, status

from src.core.trainings.fixtures.exercise import fill_exercises
from src.core.trainings.fixtures.training_types import fill_training_types

router = APIRouter()


@router.get("/import", status_code=status.HTTP_200_OK)
async def import_data() -> Response:
    await fill_exercises()
    await fill_training_types()
    return Response(status_code=status.HTTP_200_OK)
