import os
from uuid import uuid4
from fastapi import UploadFile
from app.core.config import settings
from app.models.file_model import UploadedFile

def save_file(file: UploadFile) -> UploadedFile:
    if not file.content_type.startswith("image/"):
        raise ValueError("Invalid file type")

    ext = file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{ext}"
    save_path = os.path.join(settings.UPLOAD_DIR, unique_name)

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    with open(save_path, "wb") as f:
        content = file.file.read()
        f.write(content)

    return UploadedFile(filename=unique_name, path=f"/uploads/{unique_name}")
