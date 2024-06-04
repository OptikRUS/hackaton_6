from typing import Any

from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    status: int
    message: str | None = None
    headers: dict[str, Any] | None = None

    def __init__(self) -> None:
        super().__init__(status_code=self.status, detail=self.message, headers=self.headers)
