from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

chat_cohere = os.getenv("COHERE_API_KEY")
print(chat_cohere)
model = ChatCohere()
app = FastAPI()

users = [
    {
        "id": 1,
        "username": "guille",
        "age": "19",
        "email": "guille@gmail.com"
    },
    {
        "id": 2,
        "username": "vincenzo",
        "age": "22",
        "email": "vincenzo@gmail.com"
    },
    {
        "id": 3,
        "username": "weyes",
        "age": "20",
        "email": "jose@gmail.com"
    }
]


@app.get("/")
def hello_world():
    return {"message": "Hello World"}

# get all users
@app.get(
        "/users",
        )
def get_users() -> dict:
    return {
        "messages": "succesfully fetched all users",
        "data": users
    }

class User(BaseModel):
    username: str
    age: int
    email: str



# get user by id
@app.get(
        "/users/{user_id}",
        )
def get_user(user_id: int) -> dict:
    for user in users:
        if user["id"] == user_id:
            return {
                "messages": "succesfully fetched user",
                "data": user
            }
    raise HTTPException(status_code=404, detail="User not found")


@app.post(
        "/users",
        )
def create_user(user: User) -> dict:
    user_data = user.model_dump()
    return {
        "messages": "succesfully created user",
        "data": user
    }





class Bot(BaseModel):
    prompt: str


@app.post(
        "/prompt",
        )
def create_prompt(prompt: Bot):
    user_prompt = prompt.model_dump()
    response = model.invoke("hola como estas?")
    print(response)
    return 

