import os

ALLOWED_MIME_TYPES = ["video/mp4", "images/jpeg", "images/png", "image/jpeg", "image/png"]
ALLOWED_EXTENSIONS = [".mp4", ".jpg", ".jpeg", ".png"]


def validate_file_type(content_type: str, file_name: str):
    if content_type not in ALLOWED_MIME_TYPES:
        return False
    ext = os.path.splitext(file_name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False
    return True
