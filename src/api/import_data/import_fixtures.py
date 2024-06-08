from fastapi import APIRouter, Response, status

from src.core.trainings.fixtures.exercise import fill_exercises
from src.core.trainings.fixtures.training_types import fill_training_types
from src.core.users.fixtures.users import fill_clients, fill_trainers

router = APIRouter(prefix="/import", tags=["import"])


@router.get("/data", status_code=status.HTTP_200_OK)
async def import_data() -> Response:
    await fill_exercises()
    await fill_training_types()
    return Response(status_code=status.HTTP_200_OK)


@router.get("/clients/{count}", status_code=status.HTTP_200_OK)
async def import_clients(count: int) -> Response:
    await fill_clients(count=count)
    return Response(status_code=status.HTTP_200_OK)


@router.get("/trainers/{count}", status_code=status.HTTP_200_OK)
async def import_trainers(count: int) -> Response:
    await fill_trainers(count=count)
    return Response(status_code=status.HTTP_200_OK)
