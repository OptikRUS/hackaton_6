from fastapi import APIRouter, Response, status

from src.core.trainings.fixtures.exercise import fill_exercises

router = APIRouter()


@router.get("/import", status_code=status.HTTP_200_OK)
async def import_data() -> Response:
    await fill_exercises()
    return Response(status_code=status.HTTP_200_OK)
