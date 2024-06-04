from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


async def common_exception_handler(request: Request, exception: HTTPException) -> JSONResponse:
    # logging.error(
    #     request.url.path,
    #     extra={
    #         "method": request.method,
    #         "status_code": exception.status_code,
    #         "detail": exception.detail,
    #     },
    # )

    headers = getattr(exception, "headers", None)
    status_code = getattr(exception, "status", status.HTTP_400_BAD_REQUEST)
    content_data = {
        "message": getattr(exception, "message", "Ошибка."),
        "reason": getattr(exception, "reason", "error"),
    }

    return JSONResponse(status_code=status_code, content=content_data, headers=headers)
