from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
import requests

app = FastAPI()

# ====== Keycloak UAT Config ======
KEYCLOAK_URL = "https://uat-beprc.oss.net.bd/idp/"
REALM = "BEPRC"
CLIENT_ID = "beprc-public"  # your Keycloak public client
EXPECTED_AUDIENCE = "account"  # 🔥 from your token payload

# Get OIDC configuration
oidc_config_url = f"{KEYCLOAK_URL}realms/{REALM}/.well-known/openid-configuration"
oidc_config = requests.get(oidc_config_url).json()
jwks_uri = oidc_config["jwks_uri"]
issuer = oidc_config["issuer"]
jwks = requests.get(jwks_uri).json()

# OAuth2 bearer token (used by Swagger too)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=oidc_config["token_endpoint"])

# ====== Token Verification ======
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        header = jwt.get_unverified_header(token)
        key = next(k for k in jwks["keys"] if k["kid"] == header["kid"])

        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=EXPECTED_AUDIENCE,  # ✅ must match your token's 'aud'
            issuer=issuer,
        )

        # Optional: validate azp manually (recommended for public clients)
        if payload.get("azp") != CLIENT_ID:
            raise HTTPException(status_code=401, detail="Client ID mismatch")

        return payload
    except Exception as e:
        print("TOKEN ERROR:", str(e))  # Debug print
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

# ====== Routes ======
@app.get("/")
def public():
    return {"message": "✅ This is a public route — no auth required"}


@app.get("/users", dependencies=[Depends(verify_token)])
def get_user_list():
    return {"message": "✅ This is a user list route — auth required",}

@app.get("/protected")
def protected_route(user=Depends(verify_token)):
    return {
        "message": "🔐 You are authenticated!",
        "name": user.get("name"),
        "roles": user.get("realm_access", {}).get("roles", []),
        "email": user.get("email"),
        # "data":user
    }
