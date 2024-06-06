from fastapi import APIRouter

from src.api.health import health
from src.api.import_data.import_fixtures import router as import_router
from src.core.chats.api.messages import router as chats_router
from src.core.media.api.media import router as s3_router
from src.core.trainings.api.trainings import router as trainings_router
from src.core.users.api.users import router as users_router

root_router = APIRouter()
root_router.include_router(health.router, include_in_schema=False)
root_router.include_router(users_router, include_in_schema=True)
root_router.include_router(trainings_router, include_in_schema=True)
root_router.include_router(chats_router, include_in_schema=True)
root_router.include_router(s3_router, include_in_schema=True)
root_router.include_router(import_router, include_in_schema=True)
