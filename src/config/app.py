import uvicorn
from fastapi import FastAPI

from src.api.exception_handler import common_exception_handler
from src.api.routers import root_router
from src.common.exceptions import BaseHTTPException
from src.config.initializers import init_cors, init_database, init_s3_bucket
from src.config.settings import settings


async def init_app() -> FastAPI:
    """Initialize the FastAPI application with all dependencies."""
    app = FastAPI(
        title=settings.APP.NAME,
        openapi_prefix=settings.APP.OPENAPI_PREFIX,
        version=settings.APP.VERSION,
    )
    app.include_router(root_router)
    app.add_exception_handler(BaseHTTPException, common_exception_handler)
    # await init_s3_bucket()
    init_database(app)
    init_cors(app)
    return app


async def run_api(app: FastAPI) -> None:
    """Start the FastAPI application and Uvicorn."""
    uvicorn_config = uvicorn.Config(
        app,
        host=settings.APP.ADDRESS,
        port=settings.APP.PORT,
    )
    server = uvicorn.Server(uvicorn_config)
    await server.serve()


async def main() -> None:
    """Main entry point."""
    app = await init_app()
    await run_api(app=app)
