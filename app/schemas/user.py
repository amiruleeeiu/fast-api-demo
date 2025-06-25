from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class UserProfile(BaseModel):
    username: str
    email: str
    firstName: str = ""
    lastName: str = ""
