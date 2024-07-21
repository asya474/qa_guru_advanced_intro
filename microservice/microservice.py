from fastapi import FastAPI
from datetime import datetime
import random
from models.get_single_user import SupportData,UserData,UserResponse
from models.post_create import User, UserResponse
from models.post_register import LoginRequest, LoginResponse
from models.put_update import UserUpdateRequest, UserUpdateResponse

app = FastAPI()

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": "User deleted successfully"}

@app.get("/api/users/2", response_model=UserResponse)
def get_user():
    user_data = UserData(
        id=2,
        email="janet.weaver@reqres.in",
        first_name="Janet",
        last_name="Weaver",
        avatar="https://reqres.in/img/faces/2-image.jpg"
    )
    support_data = SupportData(
        url="https://reqres.in/#support-heading",
        text="To keep ReqRes free, contributions towards server costs are appreciated!"
    )
    return UserResponse(data=user_data, support=support_data)

@app.post("/users", response_model=UserResponse)
async def create_user(user: User):
    user_id = str(random.randint(100, 999))  # Генерация случайного ID
    created_at = datetime.utcnow().isoformat() + "Z"  # Текущая дата и время в формате ISO
    return UserResponse(name=user.name, job=user.job, id=user_id, createdAt=created_at)

@app.post("/login", response_model=LoginResponse)
async def login(login_request: LoginRequest):
    return LoginResponse(id=4, token="QpwL5tke4Pnpja7X4")

@app.put("/users", response_model=UserUpdateResponse)
async def update_user(user_update: UserUpdateRequest):
    updated_at = datetime.utcnow().isoformat() + "Z"  # Текущая дата и время в формате ISO
    return UserUpdateResponse(name=user_update.name, job=user_update.job, updatedAt=updated_at)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)