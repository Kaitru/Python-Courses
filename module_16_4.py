from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users/")
async def get_all_users() -> list:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=3, max_length=15, description="Enter Username", example="John")],
                   age: Annotated[int, Path(ge=1, le=100, description="Enter Age", example=25)]) -> User:
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str,
                      username: Annotated[str, Path(min_length=3, max_length=15, description="Enter Username", example="John")],
                      age: Annotated[int, Path(ge=1, le=100, description="Enter Age", example=25)]) -> User:
    try:
        updated_user = User(id=int(user_id), username=username, age=age)
        users[int(user_id) - 1] = updated_user
        return updated_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> User:
    for user in users:
        if user.id == int(user_id):
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
