from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.schemas.user import UserProfile

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/profile", response_model=UserProfile)
def profile(user: dict = Depends(get_current_user)):
    return {
        "username": user.get("preferred_username"),
        "email": user.get("email"),
        "firstName": user.get("given_name", ""),
        "lastName": user.get("family_name", "")
    }
