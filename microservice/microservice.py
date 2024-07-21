from fastapi import FastAPI
from datetime import datetime
import random
from models.get_single_user import GetUserResponse
from models.post_create import User, UserResponse
from models.put_update import UserUpdateRequest, UserUpdateResponse

app = FastAPI()


@app.get("/api/users/{user_id}", response_model=UserResponse, status_code=200)
def get_user(user_id: int):
    # Здесь вы должны вернуть реального пользователя, например:
    return GetUserResponse(
        data=models.get_single_user.UserData(
            id=user_id,
            email=f"user{user_id}@example.com",
            first_name=f"User{user_id}",
            last_name="Example",
            avatar=f"https://reqres.in/img/faces/{user_id}-image.jpg",
        ),
        support=models.get_single_user.SupportData(
            url="https://reqres.in/#support-heading",
            text="To keep ReqRes free, contributions towards server costs are appreciated!",
        ),
    )


@app.post("/api/users", response_model=UserResponse, status_code=201)
def create_user(user: User):
    return UserResponse(
        name=user.name,
        job=user.job,
        id=str(random.randint(100, 999)),
        createdAt=datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
    )


@app.put("/api/users/{user_id}", response_model=UserUpdateResponse, status_code=200)
def update_user(user_id: int, user_update: UserUpdateRequest):
    updated_at = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
    return UserUpdateResponse(name=user_update.name, job=user_update.job, updatedAt=updated_at)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
