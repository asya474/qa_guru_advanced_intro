from pydantic import BaseModel
import dataclasses


@dataclasses.dataclass
class User(BaseModel):
    name: str
    job: str

@dataclasses.dataclass
class UserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str