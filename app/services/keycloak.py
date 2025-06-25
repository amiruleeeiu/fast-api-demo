from app.config import keycloak_openid, keycloak_admin

def authenticate_user(username: str, password: str):
    return keycloak_openid.token(username, password)

def register_user(data):
    return keycloak_admin.create_user({
        "email": data.email,
        "username": data.username,
        "enabled": True,
        "credentials": [{"value": data.password, "type": "password"}]
    })
