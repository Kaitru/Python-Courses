from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dic:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id: int) -> dic:
    return {"message": f"Вы вошли как пользователь №{user_id}"}

@app.get("/user")
async def user_page(username: str, age: int) -> dic:
    return {"message": f"Информация о пользователе. Имя: {username}. Возраст: {age}."}
