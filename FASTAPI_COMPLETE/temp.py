from fastapi import FastAPI
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field
# ! Async is a very useful tool, when you are doing task that is I/O bound, when you are fetching the information from the server and at that time, the cpu is not doing anything.
# ! We can assign the CPU some other task to complete.
# ! You can switch between the tasks quickly to work in a more efficient way.
# ! FastAPI can do things asynchronously and efficiently.

api = FastAPI()



class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description="Name of the todo")
    todo_description: str = Field(..., description="description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")

class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique identifier of todo")

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description="Name of the todo")
    todo_description: Optional[str] = Field(None, description="description of the todo")
    priority: Optional[Priority] = Field(None, description="Priority of the todo")















all_todos = [
    Todo(todo_id=1, todo_name='Sports', todo_description='Go to the Gym', priority=Priority.MEDIUM),
    Todo(todo_id=2, todo_name='Read', todo_description='Read 10 pages', priority=Priority.LOW),
    Todo(todo_id=3, todo_name='Shop', todo_description='Go shopping', priority=Priority.HIGH),
    Todo(todo_id=4, todo_name='Study', todo_description='study for exam', priority=Priority.MEDIUM),
    Todo(todo_id=5, todo_name='Meditate', todo_description='mediate 20 minutes', priority=Priority.LOW)

]


# ? If you are requesting data from the database, it still does not have to be an asynchronous method, it depends on the kind of database request/ engine and database request.
# ! If You are loading a large amount of data and, it takes time, then it makes sense to use the asynchronous request.
# ! you can mix and match synchronous and asynchronous functions depending on your needs.
# todo: FastAPI is running on starlight, it is still going to do things asynchronous even if you have defined functions synchronously. there is still going to be speed up.


@api.get("/")
def index():
    return {"message": "great"}


# Path parameter is the information that I can use inside my function.
@api.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo


# Query parameter is also defined in URL, but it is not a path
@api.get("/todos", response_model=List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    new_todo = Todo(todo_id=new_todo_id, todo_name=todo.todo_name, todo_description=todo.todo_description)
    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return updated_todo


@api.delete("/todos/{todo_id", response_model=Todo)
def delete_todo(todo_id: int):
    for index,todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo




