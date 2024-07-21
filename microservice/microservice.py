from fastapi import FastAPI
from datetime import datetime
import random
from models.get_single_user import SupportData, UserData, UserResponse
from models.post_create import User, UserResponse
from models.put_update import UserUpdateRequest, UserUpdateResponse

app = FastAPI()


@app.get("api/users/{user_id}}", response_model=UserResponse, status_code=200)
async def get_user(user_id: int):
    return UserResponse


@app.post("/api/users", response_model=UserResponse, status_code=201)
async def create_user(user: User): # Текущая дата и время в формате ISO
    return  UserResponse(
        name=user.name,
        job=user.job,
        id=str(random.randint(100, 999)),
        createdAt=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
    )

@app.put("api/users/{user_id}", response_model=UserUpdateResponse, status_code=200)
async def update_user(user_update: UserUpdateRequest):
    updated_at = datetime.utcnow().isoformat() + "Z"  # Текущая дата и время в формате ISO
    return UserUpdateResponse(name=user_update.name, job=user_update.job, updatedAt=updated_at)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
