from pydantic import BaseModel
import dataclasses


@dataclasses.dataclass
class LoginRequest(BaseModel):
    email: str
    password: str


@dataclasses.dataclass
class LoginResponse(BaseModel):
    id: int
    token: str
