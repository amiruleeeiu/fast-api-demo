from fastapi import APIRouter, HTTPException
from app.schemas.user import LoginRequest, RegisterRequest
from app.services import keycloak

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: LoginRequest):
    try:
        token = keycloak.authenticate_user(data.username, data.password)
        return token
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/register")
def register(data: RegisterRequest):
    print("Registering user with data:", data)
    try:
        user_id = keycloak.register_user(data)
        return {"message": "User registered", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
