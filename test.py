from fastapi import FastAPI
from pydantic import BaseModel

class Numbers(BaseModel):
    a: int
    b: int

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/selva/add") #exposing the api with the path /selva/add
def add(a:int,b:int):
    return a+b

@app.post("/selva/sub") #exposing the api with the path /selva/sub and accepting the data in the form of json
def sub(data: Numbers):
    return data.a - data.b
    
    
user_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35}
}

@app.get("/selva/user_db") #exposing the api with the path /users and accepting the data in the form of json
def user_database():
    return user_db

@app.get("/selva/data/{user_id}") #exposing the api with the path /users/{user_id} and accepting the data in the form of json
def get_user(user_id: int):
    if user_id in user_db:
        return user_db[user_id]
    else:
        return {"message": "User not found"}

@app.put("/selva/data/update/{user_id}") #exposing the api with the path /users/{user_id} and accepting the data in the form of json
def update_user(user_id: int, user_data: User):
    if user_id in user_db:
        user_db[user_id] = user_data.dict()
        return {"message": "User updated successfully"}
    else:
        return {"message": "User not found"}    

@app.delete("/selva/data/delete/{user_id}") #exposing the api with the path /users/{user_id} and accepting the data in the form of json
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}


print(add(3,4))