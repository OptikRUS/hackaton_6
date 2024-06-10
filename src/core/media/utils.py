import datetime
import hashlib
from collections.abc import AsyncGenerator


async def streaming_file(data: bytes, chunk_size: int) -> AsyncGenerator[str, None]:
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


def generate_valid_file_path(content_type: str, file_name: str, folder_name: str | int) -> str:
    new_file_name = hashlib.sha256(f"{datetime.datetime.now()}_{file_name}".encode()).hexdigest()
    file_path = f"{folder_name}/{new_file_name}.{content_type.split("/")[1]}"

    return file_path
