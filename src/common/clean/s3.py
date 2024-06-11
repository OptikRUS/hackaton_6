import asyncio

from src.common.s3.s3_client import s3_context
from src.config.settings import settings


async def drop_s3() -> None:
    async with s3_context() as s3:
        paginator = s3.get_paginator('list_objects')
        async for result in paginator.paginate(Bucket=settings.S3.BUCKET_NAME):
            if result.get('Contents') is not None:
                tasks = list()
                for key in result['Contents']:
                    tasks.append(
                        asyncio.create_task(
                            s3.delete_object(Bucket=settings.S3.BUCKET_NAME, Key=key['Key'])
                        )
                    )
                for i in range(0, len(tasks), 15):
                    await asyncio.gather(*tasks[i: i + 15])
