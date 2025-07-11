from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import keycloak_openid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return keycloak_openid.userinfo(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
