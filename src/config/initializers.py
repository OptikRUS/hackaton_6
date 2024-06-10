from botocore.exceptions import ClientError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.common.s3.s3_client import s3_context
from src.config.database import DATABASE_SETTINGS
from src.config.settings import settings


def init_database(app: FastAPI) -> None:
    from tortoise.contrib.fastapi import register_tortoise

    register_tortoise(
        app=app,
        db_url=DATABASE_SETTINGS["connections"]["default"],
        modules=DATABASE_SETTINGS["apps"]["models"],
        generate_schemas=True,
    )


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=settings.CORS.CREDENTIALS,
        allow_methods=settings.CORS.METHODS,
        allow_headers=settings.CORS.HEADERS,
        allow_origins=settings.CORS.ORIGINS,
    )


async def init_s3_bucket() -> None:
    async with s3_context() as s3_client:
        try:
            await s3_client.create_bucket(Bucket=settings.S3.BUCKET_NAME)
            # logger.warning(f"Bucket {settings.S3.BUCKET_NAME} created.")
        except ClientError as e:
            if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
                # logger.warning(f"Bucket {settings.S3.BUCKET_NAME} already exists.")
                pass
            else:
                raise e
