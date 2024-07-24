from pydantic import BaseModel
import dataclasses



class UserUpdateRequest(BaseModel):
    name: str
    job: str



class UserUpdateResponse(BaseModel):
    name: str
    job: str
    updatedAt: str
