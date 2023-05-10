from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = {
    1: {
        "title": "task 1",
        "description": "this is the first task",
        "created": "March 13, 2023 at 11:35:51 PM UTC+7",
        "completed": True
    },
    2: {
        "title": "task 2",
        "description": "this is the second task",
        "created": "March 13, 2023 at 11:35:51 PM UTC+7",
        "completed": False
    },
    3: {
        "title": "task 3",
        "description": "this is the third task",
        "created": "March 13, 2023 at 11:35:51 PM UTC+7",
        "completed": True
    }
}


class Todos(BaseModel):
    title: str = None
    description: str = None
    created: str = None
    completed: bool = False

# test API Endpoint for index
# in this endpoint I also return the number of data


@app.get("/")
def index():
    return {"n_todo": len(todos)}

# Endpoint GET todo lists


@app.get("/todos")
def get_todos():
    return todos

# Endpoint POST todo based on todo_ID


@app.post("/todos/{todo_id}")
def post_todos(todo_id: str, todo: Todos):
    if todo_id in todos:
        return {"error": "student ID is EXIST"}
    todos[todo_id] = todo
    return todos[todo_id]
