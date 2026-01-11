from fastapi import FastAPI
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field
# ! Async is a very useful tool, when you are doing task that is I/O bound, when you are fetching the information from the server and at that time, the cpu is not doing anything.
# ! We can assign the CPU some other task to complete.
# ! You can switch between the tasks quickly to work in a more efficient way.
# ! FastAPI can do things asynchronously and efficiently.

api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the Gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Go shopping'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'study for exam'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': 'mediate 20 minutes'}

]


# ? If you are requesting data from the database, it still does not have to be an asynchronous method, it depends on the kind of database request/ engine and database request.
# ! If You are loading a large amount of data and, it takes time, then it makes sense to use the asynchronous request.
# ! you can mix and match synchronous and asynchronous functions depending on your needs.
# todo: FastAPI is running on starlight, it is still going to do things asynchronous even if you have defined functions synchronously. there is still going to be speed up.


@api.get("/")
def index():
    return {"message": "great"}


# Path parameter is the information that I can use inside my function.
@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return {'message': todo}


# Query parameter is also defined in URL, but it is not a path
@api.get("/todos")
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo["todo_id"] for todo in all_todos) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo["todo_name"],
        'todo_description': todo['todo_description']
    }
    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            todo["todo_name"] = updated_todo["todo_name"]
            todo["todo_description"] = updated_todo["todo_description"]
            return updated_todo


@api.delete("/todos/{todo_id")
def delete_todo(todo_id: int):
    for index,todo in enumerate(all_todos):
        if todo["todo_id"] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo




