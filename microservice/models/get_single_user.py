from pydantic import BaseModel
import dataclasses
@dataclasses.dataclass
class SupportData(BaseModel):
    url: str

@dataclasses.dataclass
class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
    text: str
@dataclasses.dataclass
class GetUserResponse(BaseModel):
    data: UserData
    support: SupportData