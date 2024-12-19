from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=12)]):
    return {"message": f"Вы вошли как пользователь №{user_id}"}

@app.get("/user/{username}/{age}")
async def user_page(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="John")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter Age", example=25)]):
    return {"message": f"Информация о пользователе. Имя: {username}. Возраст: {age}."}