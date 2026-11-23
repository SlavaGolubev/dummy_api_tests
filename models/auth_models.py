from pydantic import BaseModel


class ErrorResponse(BaseModel):
    message: str


class LoginResponse(BaseModel):
    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str
    accessToken: str
    refreshToken: str

class UserMeResponse(BaseModel):
    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str