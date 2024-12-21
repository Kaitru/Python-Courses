from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users/")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=3, max_length=15, description="Enter Username", example="John")],
                   age: Annotated[int, Path(ge=1, le=100, description="Enter Age", example=25)]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {current_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, description="Enter User ID", example=1)],
                      username: Annotated[str, Path(min_length=3, max_length=15, description="Enter Username", example="John")],
                      age: Annotated[int, Path(ge=1, le=100, description="Enter Age", example=25)]) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description="Enter User ID", example=1)]) -> str:
    users.pop(str(user_id))
    return f"User {user_id} is deleted"