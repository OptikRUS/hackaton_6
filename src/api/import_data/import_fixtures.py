from fastapi import APIRouter, Response, status
from tortoise.transactions import in_transaction

from src.common.clean.database import drop_database
from src.common.clean.s3 import drop_s3
from src.core.trainings.fixtures.exercise import fill_exercises
from src.core.trainings.fixtures.training_templates import fill_training_templates
from src.core.trainings.fixtures.training_types import fill_training_types
from src.core.users.fixtures.users import fill_clients, fill_trainers

router = APIRouter(prefix="/import", tags=["import"])


@router.get("/data", status_code=status.HTTP_200_OK)
async def import_data() -> Response:
    await fill_training_types()
    await fill_exercises()
    return Response(status_code=status.HTTP_200_OK)


@router.get("/clients/{count}", status_code=status.HTTP_200_OK)
async def import_clients(count: int) -> Response:
    await fill_clients(count=count)
    return Response(status_code=status.HTTP_200_OK)


@router.get("/trainers/{count}", status_code=status.HTTP_200_OK)
async def import_trainers(count: int) -> Response:
    await fill_trainers(count=count)
    return Response(status_code=status.HTTP_200_OK)


@router.delete(
    "/data",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_all_info() -> Response:
    await drop_database()
    await drop_s3()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/templates/{count}", status_code=status.HTTP_200_OK)
async def import_templates(count: int) -> Response:
    await fill_training_templates(count=count)
    return Response(status_code=status.HTTP_200_OK)
