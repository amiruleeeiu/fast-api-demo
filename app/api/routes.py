from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.file_schema import FileUploadResponse
from app.services.file_service import save_file

router = APIRouter()

@router.post("/upload-image", response_model=FileUploadResponse)
async def upload_image(image: UploadFile = File(...)):
    try:
        uploaded = save_file(image)
        return FileUploadResponse(filename=uploaded.filename, path=uploaded.path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
