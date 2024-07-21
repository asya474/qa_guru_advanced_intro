from pydantic import BaseModel

class SupportData(BaseModel):
    url: str

class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
    text: str
class UserResponse(BaseModel):
    data: UserData
    support: SupportData