from fastapi import FastAPI
from datetime import datetime
import random
from models.get_single_user import UserResponse as GetUserResponse, UserData as GetUserData, SupportData as GetSupportData
from models.post_create import User, UserResponse
from models.put_update import UserUpdateRequest, UserUpdateResponse

app = FastAPI()


@app.get("/api/users/{user_id}", response_model=GetUserResponse, status_code=200)
def get_single_user(user_id: int):
    # Здесь вы должны вернуть реального пользователя, например:
    return GetUserResponse(
        data=GetUserData(
            id=user_id,
            email=f"user{user_id}@example.com",
            first_name=f"User{user_id}",
            last_name="Example",
            avatar=f"https://reqres.in/img/faces/{user_id}-image.jpg",
            text="To keep ReqRes free, contributions towards server costs are appreciated!",
        ),
        support=GetSupportData(
            url="https://reqres.in/#support-heading",
        ),
    )


@app.post("/api/users", response_model=UserResponse, status_code=201)
def post_create_user(user: User):
    user_id = str(random.randint(100, 999))
    user=User(name="User"+user_id, job="Job"+user_id)
    return UserResponse(
        name=user.name,
        job=user.job,
        id=user_id,
        createdAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
    )


@app.put("/api/users/{user_id}", response_model=UserUpdateResponse, status_code=200)
def put_update_user(user_id: int, user_update: UserUpdateRequest):
    user_id = str(random.randint(100, 999))
    user_update = UserUpdateRequest(name="User"+user_id, job="Job"+user_id)
    updated_at = datetime.now().isoformat() + "Z"
    return UserUpdateResponse(
        name=user_update.name,
        job=user_update.job,
        updatedAt=updated_at)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
