from pydantic import BaseModel
import dataclasses


@dataclasses.dataclass
class UserUpdateRequest(BaseModel):
    name: str
    job: str


@dataclasses.dataclass
class UserUpdateResponse(BaseModel):
    name: str
    job: str
    updatedAt: str
