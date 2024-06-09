from typing import AsyncGenerator


async def streaming_file(
    data: bytes, chunk_size: int
) -> AsyncGenerator[str, None]:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]
